import os

def load_docs(folder_path):
    """加载本地知识库文件"""
    documents = []
    if not os.path.exists(folder_path):
        print(f"错误：找不到文件夹{folder_path}")
        return documents
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            path = os.path.join(folder_path, filename)
            #指定utf-8，避免读中文乱码
            with open(path, 'r',encoding='utf-8') as f:
                content = f.read()
                documents.append(content)
                print(f"成功加载文件:{filename}")
    return documents

if __name__ == "__main__":
    # 尝试加载data文件夹的内容
    texts = load_docs("./data")
    print(f"一共读取了{len(texts)}个文档。")