#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:37:49 2024

@author: williamchung
"""
#建立hash
data_dict = {}

#讀取檔案中的資料
with open('hw2_data.txt', 'r') as file:
    for line in file:
        key = line.strip() #移除換行
        if key not in data_dict: #檢查字是否在hash中
            data_dict[key] = 1
        else:
            data_dict[key] += 1          

print('總共出現'+str(len(data_dict.keys()))+'個不重複的英文字')
print('每個英文字出現次數:')
print(data_dict)



