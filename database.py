import chromadb
from chromadb.config import Settings
#1.初始化数据库：告诉它把数据存储在D盘哪个文件夹
client = chromadb.PersistentClient(path="./chroma_db")

#2.创建集合：相当于数据库中的表，名字叫"psychology_knowledge"
collection = client.get_or_create_collection(name="psychology_knowledge")

def save_to_database(chunks, vectors, ids):
    """
    将文本片段和对应的向量存入数据库
    """
    collection.add(
        documents=chunks,
        embeddings=vectors,
        ids=ids
    )
    print("---存储完成！---")

if __name__ == "__main__":
    #模拟测试数据
    test_chunks = ["焦虑是一种常见的情绪", "深呼吸可以缓解压力"]
    # 假设这是我们算好的简单向量（实际用时会传入 embedding.py 算出的结果）
    test_vectors = [[0.1]*384,[0.2]*384]
    test_ids = ["doc1", "doc2"] 

    save_to_database(test_chunks, test_vectors, test_ids)
    