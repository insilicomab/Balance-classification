# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:34:58 2021

@author: m-lin
"""

# ライブラリの読み込み
import pandas as pd

# テストデータの読み込み
test = pd.read_csv('test.tsv', sep='\t')

# テストデータの中身を確認する
print(test.head())
print(test.dtypes)

# 'id'の削除と確認
test = test.drop(test.columns[[0]], axis=1)
print(test.head())
print(len(test))

# testデータのclassを予測
preds = [] # 予測値を格納する空のリストを準備

for i in range(len(test)):
    l_wd = test.iloc[i,0] * test.iloc[i,1] # left_weight * left_distance
    r_wd = test.iloc[i,2] * test.iloc[i,3] # right_weight * right_distance
    
    if l_wd > r_wd: 
        preds.append(0)
        
    elif l_wd == r_wd:
        preds.append(1)
    
    elif l_wd < r_wd:
        preds.append(2)

'''
提出
'''

# 提出用データの読み込み
sub = pd.read_csv('sample_submit.csv', sep=',', header=None)
print(sub.head())
    
# 目的変数カラムの置き換え
sub[1] = preds

# ファイルのエクスポート
sub.to_csv('submission.csv', header=None, index = None)
