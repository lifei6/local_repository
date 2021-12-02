# 导入鸢尾花数据
from sklearn.datasets import load_iris, fetch_20newsgroups
# 导入seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 接受数据
# 1.获取小数据集
iris = load_iris()
# print("鸢尾花数据集的返回值：\n", iris)
# 2.获取达数据集
# newsgroups = fetch_20newsgroups(data_home=None, subset='train')
# print(newsgroups)
# 返回值是一个继承自字典的Bench
# data：特征数据数组，是 [n_samples * n_features] 的二维 numpy.ndarray 数组
# target：标签数组，是 n_samples 的一维 numpy.ndarray 数组
# DESCR：数据描述
# feature_names：特征名,新闻数据，手写数字、回归数据集没有
# target_names：标签名
# 其内容可以用索引也可以用.的形式
print("鸢尾花数据集的特征数据组：\n", iris.data)
print("鸢尾花数据集的特征名字：\n", iris['feature_names'])
print("鸢尾花数据集的目标值：\n", iris.target)
print("鸢尾花数据集的目标值的名称：\n", iris.target_names)
print("鸢尾花数据集的描述：\n", iris.DESCR)
# 图像展示鸢尾花数据
# 把数据转换成dataframe的格式
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
# 在DataFrame最后增加一列目标值
iris_df['Species'] = iris.target
# print(iris_df)


def plot_iris(iris, col1, col2):
    """
    定义一个绘图函数，进行组合绘图
    :param iris: 需要的数据
    :param col1: x
    :param col2: y
    """
    # hue是目标值，fit_reg是否线性拟合
    sns.lmplot(x=col1, y=col2, data=iris, hue="Species", fit_reg=False)
    plt.xlabel(col1, fontsize=10)
    plt.ylabel(col2, fontsize=10)
    plt.title('鸢尾花种类分布图', fontsize=20)
    plt.show()


plot_iris(iris_df, iris.feature_names[1], iris.feature_names[0])


