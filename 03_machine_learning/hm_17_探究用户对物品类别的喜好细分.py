import pandas as pd
# TODO 太大了去jupyter
# 1.获取数据
aisles = pd.read_csv('./data/instacart/aisles.csv')
order_product = pd.read_csv('./data/instacart/order_products__prior.csv')
orders = pd.read_csv('./data/instacart/orders.csv')
products = pd.read_csv('./data/instacart/products.csv')
print(aisles.head())
# 2.数据基本处理
# 2.1 合并表格
# 2.2 交叉表合并
# 2.3 数据截取
# 3.特征工程 — pca
# 4.机器学习（k-means）
# 5.模型评估
# sklearn.metrics.silhouette_score(X, labels)
# 计算所有样本的平均轮廓系数
# X：特征值
# labels：被聚类标记的目标值