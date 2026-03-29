from fastapi import FastAPI
from query import search_knowledge
from openai import OpenAI #(更新)采用本地化部署，Ollama兼容OpenAI接口
#1.创建FastAPI实例
app = FastAPI(title="智心守护RAG接口系统——本地增强版")
client = OpenAI(api_key="ollama", 
                base_url="http://localhost:11434") #(更新)指向本地4060显卡
#2.定义查询接口
@app.get("/")
def home():
    return {"message": "欢迎来到智心守护 RAG 本地 API！当前引擎：Qwen2.5:7b"}
#3.定义搜索接口，用户通过/search?query=我的问题     
@app.get("/search")
def get_search_results(q: str):
    if not q:
        return {"error": "查询参数不能为空，请提供一个问题。"}
    #复用之前写好的查询函数
    raw_results = search_knowledge(q, top_k=3)

    #格式化输出结果
    formatted_results = []
    for i in range(len(raw_results['documents'][0])):
        dist = raw_results['distances'][0][i]
        formatted_results.append({
            "content": raw_results['documents'][0][i],
            "distance": round(dist, 4)
        })
    return {"query": q, "results": formatted_results}
#4.(更新)定义一个新的对话接口，直接调用本地Qwen2.5进行问答
@app.get("/ask")
def chat_with_ai(q: str):
    #第一步：检索本地向量知识库
    search_results = search_knowledge(q, top_k=2)#先检索相关知识
    context_text = "\n".join(search_results['documents'][0])#将检索到的内容拼接成一个字符串
    print(f"\n==== 成功从 ChromaDB 中检索到的参考资料 ====\n{context}\n==========================================\n")
    # 第二步：构建 Prompt（让模型扮演专业角色）
    prompt = f"""你是一个专业的心理辅导专家。请根据以下参考资料回答用户的问题。
    
    参考资料：
    {context}
    
    用户问题：{q}
    
    要求：语气温和、专业，如果参考资料中没有相关内容，请基于你的专业知识给出建议。"""

    # 第三步：调用本地 4060 显卡进行推理
    try:
        response = client.chat.completions.create(
            model="qwen2.5:7b",  # 核心修改：必须与你下载的模型名称一致
            messages=[
                {"role": "system", "content": "你是一个温暖的心理医生。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,     # 增加人情味，让回答不那么生硬
        )
        return {
            "answer": response.choices[0].message.content,
            "source": "Local Ollama (Qwen-2.5-7B)"
        }
    except Exception as e:
        return {"error": f"本地模型调用失败，请检查 Ollama 是否启动。错误信息：{str(e)}"}