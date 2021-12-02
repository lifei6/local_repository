from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, RidgeCV, Ridge
from sklearn.metrics import mean_squared_error


def linear_model1():
    """
    线性回归：正规方程法
    :return:
    """
    # 1.获取数据
    data = load_boston()
    # print(data.data)
    # print(data.target)
    # 2.基本数据处理
    # 2.1 数据划分
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=22)
    # 3.特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.机器学习--线性回归（正规方程）
    estimator = LinearRegression(fit_intercept=True)
    estimator.fit(x_train, y_train)
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


def linear_model2():
    """
    线性回归：随机梯度下降法
    :return:
    """
    # 1.获取数据
    data = load_boston()
    # print(data.data)
    # print(data.target)
    # 2.基本数据处理
    # 2.1 数据划分
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=22)
    # 3.特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.机器学习--线性回归（梯度下降）
    # max_iter最大迭代次数，learning_rate学习率，eta0是学习率参数
    estimator = SGDRegressor(learning_rate="constant", eta0=0.01)
    estimator.fit(x_train, y_train)
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


def linear_model3():
    """
    线性回归：岭回归--ridge
    为了解决过拟合问题
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
    # 5.3模型的其他属性
    print("这个模型的最好的准确率：\n", estimator.best_score_)
    return None


if __name__ == '__main__':
    # 1.正规方程减少线性损失
    linear_model1()
    # 2.梯度下降法减少线性损失
    linear_model2()
    # 3.岭回归
    linear_model3()