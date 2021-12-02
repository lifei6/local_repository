# 特征提取是对文本或者分类名或者图片进行转换为可用于机器学习的数字特征
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
import jieba


def dict_demo():
    """
    字典特征提取-one-hot编码类似
    :return:
    """
    # 1.获取数据
    dict = [{'city': '北京', 'temperature': 100},
            {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]
    # 2.特征工程
    # 2.1 特征提取
    transfer = DictVectorizer(sparse=False)
    data = transfer.fit_transform(dict)
    data = data.astype(np.int32)
    print("返回的结果:\n", (data, data.shape))
    print("特征名字：\n", transfer.get_feature_names())
    # 3.训练模型
    # 4.模型评估
    return None


def text_demo1():
    """
    文本特征提取——英文
    返回的是词频列表——出现的次数，所以不一定都是1
    :return:
    """
    # 1.获取文本数据
    data = ["life is short short,i like python",
            "life is too long,i dislike python"]
    # 2.特征工程-文本特征提取
    # 注意文本转换器没有sparse这个属性，使用toarray()转换为数组
    # 以空格进行切分，不统计标点和单个字母
    transfer = CountVectorizer(stop_words=['is', 'too'])
    data_new = transfer.fit_transform(data)
    print("特征名称（单词）：\n", transfer.get_feature_names())
    print("返回结果：\n", data_new.toarray())
    return None


def jieba_cut_demo(data):
    """
    对中文进行分词
    :param data:
    :return:
    """
    # jieba.cut()返回的是词语组的生成器，先转为列表，在用空格链接成字符串
    new_data = " ".join(list(jieba.cut(data)))
    # print(new_data)
    return new_data


def text_demo2():
    """
    文本特征提取——中文
    返回的是词频列表——出现的次数，所以不一定都是1
    :return:
    """
    # 1.获取文本数据
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    # 2.对文本进行处理
    data_list = []
    for i in data:
        j = jieba_cut_demo(i)
        data_list.append(j)
    print("分词后的结构：\n", data_list)
    # 3.特征工程-文本特征提取
    # 注意文本转换器没有sparse这个属性，使用toarray()转换为数组
    # 以空格进行切分，不统计标点和单个字
    transfer = CountVectorizer(stop_words=['还是'])
    data_new = transfer.fit_transform(data_list)
    print("特征名称（词语）：\n", transfer.get_feature_names())
    print("返回结果：\n", data_new.toarray())
    return None


def tfidf_demo():
    """
    文本特征提取——中文
    tf-词频
    idf-逆向文档频率（词语的普遍重要程度）--文章总数除以该词出现的文章次数再取10为底的对数
    tf-idf = tf*idf
    :return:
    """
    # 1.获取文本数据
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    # 2.对文本进行处理
    data_list = []
    for i in data:
        j = jieba_cut_demo(i)
        data_list.append(j)
    print("分词后的结构：\n", data_list)
    # 3.特征工程-文本特征提取
    # transfer = CountVectorizer(stop_words=['还是'])
    transfer = TfidfVectorizer()
    data_new = transfer.fit_transform(data_list)
    print("特征名称（词语）：\n", transfer.get_feature_names())
    print("tf-idf返回结果：\n", data_new)
    return None


if __name__ == '__main__':
    # 1.字典类型的特征提取
    # dict_demo()
    # 2.英文文本特征提取
    # text_demo1()
    # 3.jieba分词函数
    # jieba_cut_demo("我爱北京天安门")
    # 4.中文文本特征提取
    # text_demo2()
    # 5.tf-idf文本特征提取
    tfidf_demo()