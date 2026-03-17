#1.导入功能
from loader import load_docs
from process import split_my_text
from embedding import get_embeddings
from database import save_to_database
def run_pipeline():
    print("=== 智心守护 RAG系统 ：启动中 ===")

    #2.调用loader加载文档
    raw_data = load_docs("./data")

    if not raw_data:
        print("未找到任何文档，请检查！")
        return
    #3.调用process 切分文本
    print(f"正在处理{len(raw_data)}份原始文档...")
    chunks = split_my_text(raw_data)

    #4.展示集成成果
    print(f"=== 集成成功！知识库已更新 ===")
    print(f"总碎片数:{len(chunks)}")
    
    #5.调用embedding获取向量
    vectors = get_embeddings(chunks)

    #6.调用database存储数据
    ids = [f"doc_{i}"for i in range(len(chunks))]#生成唯一ID
    save_to_database(chunks, vectors, ids)
    print(f"成功将{len(chunks)}个心理学知识点存入数据库！")

if __name__ == "__main__":
    run_pipeline()