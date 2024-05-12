#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:18:24 2024

@author: williamchung
"""

#氣泡排序法
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#作業list
my_list = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

#Sort
bubble_sort(my_list)
print("Sorted list:", my_list)
