#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : etest.py
# @Software: PyCharm
# @Author: Kenn
# @Date  : 2018/4/3
# @Desc  :
import numpy as np

np.random.seed(42)

a = np.round(np.random.rand(20), 4)
n1 = np.array([0, 0])
n2 = np.array([2, 2])
d = np.sum(np.square(n1 - n2))
print(a)
print(d)
