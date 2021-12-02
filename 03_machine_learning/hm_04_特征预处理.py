import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def min_max_demo():
    # 1.获取数据
    data = pd.read_csv('./data/dating.txt')
    print(data)
    # 2.实例化一个转化器类
    transfer = MinMaxScaler(feature_range=(2, 3))
    # 3.调用fit_transform()进行转换
    data = transfer.fit_transform(data[['milage', 'Liters', 'Consumtime']])
    print('归一化后的数据: \n', (data, data.shape))
    return None


def stand_demo():
    """
    标准化处理
    :return:
    """
    # 1.获取数据
    data = pd.read_csv('./data/dating.txt')
    print(data)
    # 2.实例化一个转化器类
    transfer = StandardScaler()
    # 3.调用fit_transform()进行转换
    data = transfer.fit_transform(data[['milage', 'Liters', 'Consumtime']])
    print('标准化后的数据: \n', (data, data.shape))
    print("每一列特征的平均值: \n", transfer.mean_)
    print("每一列特征值的方差: \n", transfer.var_)
    return None


if __name__ == '__main__':
    # 1.归一化处理
    # 以后不用你了
    # min_max_demo()
    # 2.标准化处理
    # 以后就用你了
    stand_demo()