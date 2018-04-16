#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dbscan.py
# @Software: PyCharm
# @Author: Kenn
# @Date  : 2018/4/16
# @Desc  : DBSCAN 算法分簇
from WsnsToplogy import WsnsToplogy
import numpy as np
from sklearn.cluster import DBSCAN


def main():
	node_num = 50
	monit_area = [100, 100]
	net = WsnsToplogy(monit_area = monit_area, node_num = node_num)
	nodes_xy = net.getNode_XY()
	cls_num = int(np.ceil(np.sqrt(node_num / 2)))  # 上取整
	print("cluster number: " + str(cls_num))
	dbscan = DBSCAN(eps = 15, min_samples = 2).fit(nodes_xy)
	cluster = dbscan.labels_
	center_xy = dbscan.core_sample_indices_
	print(cluster)
	print(center_xy)


if __name__ == '__main__':
	main()
