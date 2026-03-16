from sentence_transformers import SentenceTransformer
import time

#初始化模型（运行脚本时只执行一次）
print("---正在初始化语义模型---")

#调用paraphrase-multilingual-MiniLM-L12-v2模型，经典的中英文多语言模型

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def get_embeddings(text_list):
    """
    将文本列表转化为向量数组
    """
    if not text_list:
        print("警告：输入文本列表为空，无法生成向量。")
        return []
    
    print(f"---正在转化{len(text_list)}个文本为向量---")

    vectors = model.encode(text_list, show_progress_bar=True)#将字符串转化为浮点数数组，显示进度条

    return vectors

if __name__ == "__main__":
    #模拟数据测试
    test_sentences = ["我最近总是感到无缘无故的心慌。",
        "这种焦虑的情绪影响了我的睡眠。",
        "今天中午想去食堂吃红烧肉。"]
    
    start = time.time()

    #调用函数获取向量

    result_vectors = get_embeddings(test_sentences)

    #打印详情
    print(f"\n[运行成功] 耗时：{time.time() - start:.4f}秒")
    print(f"[向量维度]：{len(result_vectors[0])}维")#每个片段被转化成384个数字
    print(f"[数据示例]：{result_vectors[0][:3]}...")#展示第一个片段的前3个数字