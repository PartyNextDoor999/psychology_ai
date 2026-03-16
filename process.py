from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_my_text(text_list):
    """将读取到的文档列表切分成碎片"""
    #初始化切分器
    #chunk_size:每个碎片的字数限制（这里设置为100字左右）
    #chunk_overlap:碎片之间的重叠字数（这里设置为20字，确保上下文连贯）
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100, 
        chunk_overlap=20,
        separators=["\n\n","\n","。","！","?"," ",""]
        )
    #这里的text_list 是从loader.py拿到的文档内容列表
    #将它们合并成一个大字符串处理
    combined_text = "\n".join(text_list)
    chunks = splitter.split_text(combined_text)

    return chunks
if __name__ == "__main__":
    #模拟从loader拿到的数据
    test_data =["心理学是研究行为和心理变化规律的科学。它涉及人类的认知、情感、动机等方面。心理学的应用非常广泛，包括临床心理学、教育心理学、工业心理学等领域。通过心理学的研究，我们可以更好地理解自己和他人，提升生活质量。"
                "心理学包含很多分支，如认知心理学、发展心理学、社会心理学等。每个分支都有其独特的研究对象和方法。心理学的研究方法包括实验法、观察法、调查法等，这些方法帮助我们系统地探索心理现象。"]
    result = split_my_text(test_data)

    print(f"切分完成，得到了{len(result)}个碎片。")

    for i, chunk in enumerate(result):
        print(f"片段{i+1}:{chunk}")