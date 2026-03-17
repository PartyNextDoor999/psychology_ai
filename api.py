from fastapi import FastAPI
from query import search_knowledge
from openai import OpenAI #新加入，调用api实现问答功能
#1.创建FastAPI实例
app = FastAPI(title="智心守护RAG接口系统")
client = OpenAI(api_key="sk-8b64f84643ef474e943b9cdfa796f579", 
                base_url="https://api.deepseek.com") #初始化OpenAI客户端
#2.定义查询接口
@app.get("/")
def home():
    return {"message": "欢迎来到智心守护RAG API 已启动"}
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
#4.定义一个新的对话接口，直接调用DS的API进行问答
@app.get("/ask")
def chat_with_ai(q: str):
    search_results = search_knowledge(q, top_k=3)#先检索相关知识
    context_text = "\n".join(search_results['documents'][0])#将检索到的内容拼接成一个字符串

    messages = [
       {"role": "system", "content": "你是一位温暖专业的心理咨询师。请结合【参考资料】回答，如果资料没提，请用你的专业知识补齐。"},
       {"role": "user", "content": f"【参考资料】：\n{context_text}\n\n【用户问题】：{q}"}
    ]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    #返回最终答案
    return {
        "answer": response.choices[0].message.content,
        "source": search_results['documents'][0] #附上检索到的内容作为参考
    }