import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
# 1.获取数据
train = pd.read_csv('./data/titanic/train.csv')
test = pd.read_csv('./data/titanic/test.csv')
# 2.数据基本处理
# 2.1 确定特征值，目标值
x_train = train[['Pclass', 'Sex', 'Age']]
y_train = train['Survived']
# x_test = test[['Pclass', 'Sex', 'Age']]
# 2.2 缺失值处理
# 判断是否有缺失值
# print(np.all(pd.notna(x_train)))
# 进行年龄缺失值的平均替换
x_train['Age'].fillna(value=x_train['Age'].mean(), inplace=True)
# x_test['Age'].fillna(value=x_test['Age'].mean(), inplace=True)
# 2.3 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=22)
# 3.特征工程--字典特征提取
transfer = DictVectorizer(sparse=False)
# 注意这里的特征值必须是字典类型
x_train = transfer.fit_transform(x_train.to_dict(orient="record"))
x_test = transfer.transform(x_test.to_dict(orient="records"))
print("特征提取结果：\n", x_train)
print("特征名字：\n", transfer.get_feature_names())
# 4.机器学习--随机森林分类--集成学习
estimator = RandomForestClassifier(n_estimators=120, criterion="gini", max_depth=5, min_samples_leaf=2)
# 设置超参数字典进行交叉验证网格搜索
param = {"n_estimators": [30, 50, 80],
         "max_depth": [7, 10, 12],
         "min_samples_leaf": [1, 2, 4],
         }
estimator = GridSearchCV(estimator, param, cv=2)
estimator.fit(x_train, y_train)
# 5.模型评估
# 5.1 预测结果及准确性
y_predict = estimator.predict(x_test)
print("真实值与预测值的对比：\n", y_predict == y_test)
score = estimator.score(x_test, y_test)
print("模型准确性：\n", score)
# 5.2 该模型的属性
print("这个模型的最好参数设置是：\n", estimator.best_estimator_)
# 6.决策树可视化
# export_graphviz(estimator, out_file="./data/titanic/tree.dot", feature_names=['Age', 'Pclass', 'Sex=female', 'Sex=male'])