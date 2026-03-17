from fastapi import FastAPI
from query import search_knowledge

#1.创建FastAPI实例
app = FastAPI(title="智心守护RAG接口系统")

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