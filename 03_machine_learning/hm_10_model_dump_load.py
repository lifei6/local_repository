from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, RidgeCV, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib


def model_dump_load():
    """
    线性回归：训练模型保存与加载
    :return:
    """
    # 1.获取数据
    data = load_boston()
    # 2.基本数据处理
    # 2.1 数据划分
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=22)
    # 3.特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.机器学习--线性回归（岭回归）
    # alpha为正则力度（0-1，1-10）
    # estimator = Ridge(alpha=1)
    estimator = RidgeCV(alphas=(0.1, 1, 10))
    estimator.fit(x_train, y_train)
    # # 4.2 模型保存
    # joblib.dump(estimator, "./data/test.pkl")
    # # 4.3 模型加载
    # estimator = joblib.load("./data/test.pkl")
    print("这个模型的系数是：\n", estimator.coef_)
    print("这个模型的偏置是：\n", estimator.intercept_)
    # 5.模型评估
    # 5.1 模型预测及准确率
    price_predict = estimator.predict(x_test)
    print("预测房价为：\n", price_predict)
    score = estimator.score(x_test, y_test)
    print("模型的准确率为：\n", score)
    # 5.2 误差分析
    mse = mean_squared_error(y_test, price_predict)
    print("mse为：\n", mse)
    return None


if __name__ == '__main__':
    # 3.岭回归
    model_dump_load()