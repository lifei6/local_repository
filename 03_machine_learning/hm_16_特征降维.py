# 特征降维有两种方式
# 1.特征选择--方差--相关系数
# 2.主成分分析--pca
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr, spearmanr
from sklearn.decomposition import PCA


def var_demo():
    """
    过滤低方差减少特征值
    :return:
    """
    data = pd.read_csv("./data/factor_returns.csv")
    print(data.head())
    transfer = VarianceThreshold(threshold=10)
    data = transfer.fit_transform(data.iloc[:, 1:10])
    print("降维后的结果：\n", data.shape)
    return None


def pea_demo():
    """
    皮尔逊相关系数
    :return:
    """
    x1 = [12.5, 15.3, 23.2, 26.4, 33.5, 34.4, 39.4, 45.2, 55.4, 60.9]
    x2 = [21.2, 23.9, 32.9, 34.1, 42.5, 43.2, 49.0, 52.8, 59.4, 63.5]
    print("看第一个返回值为相关系数：\n", pearsonr(x1, x2))
    return None


def spea_demo():
    """
    斯皮尔曼相关系数
    :return:
    """
    x1 = [12.5, 15.3, 23.2, 26.4, 33.5, 34.4, 39.4, 45.2, 55.4, 60.9]
    x2 = [21.2, 23.9, 32.9, 34.1, 42.5, 43.2, 49.0, 52.8, 59.4, 63.5]
    print("看第一个返回值为相关系数：\n", spearmanr(x1, x2))
    return None


def pca_demo():
    """
    pca主成分分析降维
    :return:
    """
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    # n_components小数表示保留百分之多少的信息，整数表示保留几个特征
    transfer = PCA(n_components=0.99)
    transfer_data = transfer.fit_transform(data)
    print("pca降维后的结果：\n", transfer_data)
    return None


if __name__ == '__main__':
    # 1.过滤式特征选择--低方差过滤
    # var_demo()
    # 2.皮尔逊相关系数
    # pea_demo()
    # 3.斯皮尔曼相关系数
    # spea_demo()
    # 4.pca降维
    pca_demo()