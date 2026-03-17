import chromadb
from embedding import get_embeddings

#1.连接到本地化数据库
client  = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="psychology_knowledge")

def search_knowledge(query_text, top_k=3):
    """
    输入问题,返回最相关的top_k个知识片段
    """
    #2.将用户的问题也转化为维度同为384的向量
    query_vector = get_embeddings([query_text])

    #3.在数据库中进行相似度搜索，返回最相关的top_k个结果
    results = collection.query(
        query_embeddings=query_vector.tolist(),#转化为列表格式
        n_results=top_k
    )
    return results
if __name__ == "__main__":
    print("=== 测试查询功能 ===")
    user_input = input("请输入你的心理学相关问题：")

    search_results = search_knowledge(user_input)

    print("\n=== 查询结果 ===")
    #遍历显示找到的内容
    for i, doc in enumerate(search_results['documents'][0]):
        #distance是相似度的一个指标，数值越小表示越相关
        distance = search_results['distances'][0][i]
        print(f"\n[匹配项{i+1}] (相似度: {1 - distance:.4f})")
        print(f"内容：{doc}")