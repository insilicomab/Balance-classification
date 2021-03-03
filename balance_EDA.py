# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:53:07 2021

@author: m-lin
"""

# ライブラリの読み込み
import pandas as pd
from sklearn.metrics import accuracy_score

# データの読み込み
train = pd.read_csv('train.tsv', sep='\t')

# データの確認
print(train.head())

# 'id'の削除と確認
train = train.drop(train.columns[[0]], axis=1)
print(train.head())
print(train.shape)

print(train.iloc[0,0])

# trainデータのclassを予測
y_train_preds = []

for i in range(len(train)):
    l_wd = train.iloc[i,1] * train.iloc[i,2] # left_weight * left_distance
    r_wd = train.iloc[i,3] * train.iloc[i,4] # right_weight * right_distance
    
    if l_wd > r_wd:
        y_train_preds.append(0)
        
    elif l_wd == r_wd:
        y_train_preds.append(1)
    
    elif l_wd < r_wd:
        y_train_preds.append(2)

# trainデータのclass（目的変数）を取得
y_train_true = train['class']

# accuracyを計算する
score = accuracy_score(y_train_true, y_train_preds)
print(score)
