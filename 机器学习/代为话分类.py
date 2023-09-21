# -*- coding: utf-8 -*-
# time:2023/9/4 14:38
# file 代为话分类.py
# outhor:czy
# email:1060324818@qq.com

import matplotlib.pyplot as plt
import mglearn as mglearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris_dataset = load_iris()

x_train ,x_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

iris_dataframe = pd.DataFrame(x_train,columns=iris_dataset.feature_names)

grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train,figsize=(15,15),marker='0',hist_kwds={'bins':20},s=60,alpha=.8,cmap=mglearn.cm3)

knn=KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train,y_train)

pred = knn.predict(x_test)

print(np.mean(pred == y_test))

plt.show()