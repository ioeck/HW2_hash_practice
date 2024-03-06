#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:10:24 2024

@author: williamchung
"""

decimal = int(input('請輸入0~255間的數字:'))
list = []
binary = ''

if decimal > 2**8:
    print('請輸入0~255間的數字!')
else:
    for i in range(7,-1,-1):
        decimal > (2**i)
        n = decimal // (2**i)
        list.append(n)
        decimal = decimal % (2**i)
    for i in range(0,8):
        binary += str(list[i])
    print('二進位：')
    print(binary)
    
sum_1 = 0  
sum_2 = 0 
for i in range(3,-1,-1):
    sum_1 += list[0]*(2**i)
    list.pop(0)
  
if sum_1 == 10:
    sum_1 = 'A'
elif sum_1 == 11:
    sum_1 = 'B'
elif sum_1 == 12:
    sum_1 = 'C'
elif sum_1 == 13:
    sum_1 = 'D'
elif sum_1 == 14:
    sum_1 = 'E'
elif sum_1 == 15:
    sum_1 = 'F'  
  
for i in range(3,-1,-1):
    sum_2 += list[0]*(2**i)
    list.pop(0)

if sum_2 == 10:
    sum_2 = 'A'
elif sum_2 == 11:
    sum_2 = 'B'
elif sum_2 == 12:
    sum_2 = 'C'
elif sum_2 == 13:
    sum_2 = 'D'
elif sum_2 == 14:
    sum_2 = 'E'
elif sum_2 == 15:
    sum_2 = 'F'
    
print('十六進位：')
print(str(sum_1)+str(sum_2))
