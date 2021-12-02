from sklearn.linear_model import LinearRegression
# 1.构造一组学生成绩数据
x = [[80, 86],
[82, 80],
[85, 78],
[90, 90],
[86, 82],
[82, 90],
[78, 80],
[92, 94]]
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]
# 机器学习
estimator = LinearRegression()
estimator.fit(x, y)
# 输出训练模型的系数cofe_
print("线性回归系数是：\n", estimator.coef_)
# 预测
ret = estimator.predict([[100, 80]])
print("预测结果：\n", ret)