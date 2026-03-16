#1.导入功能
from loader import load_docs
from process import split_my_text

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

    #5.测试效果（展示部分内容）
    for i , chunk in enumerate(chunks[:2]):
        print(f"\n--- 碎片{i+1} ---")
        print(chunk)

if __name__ == "__main__":
    run_pipeline()