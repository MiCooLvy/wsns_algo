#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Software: PyCharm
# @Author: Kenn
# @Date  : 2018/4/3
# @Desc  :
from WsnsToplogy import WsnsToplogy
import numpy as np
from sklearn.cluster import KMeans


def main():
	node_num = 50
	monit_area = [100, 100]
	net = WsnsToplogy(monit_area = monit_area, node_num = node_num)
	# print(net.getNode_XY())
	nodes_xy = net.getNode_XY()
	cls_num = int(np.ceil(np.sqrt(node_num / 2)))  # 上取整
	print("cluster number: " + str(cls_num))
	clusterer = KMeans(n_clusters = cls_num, max_iter = 1000, random_state = 32)
	kmeans = clusterer.fit(nodes_xy)
	center_xy = kmeans.cluster_centers_
	cluster = kmeans.labels_
	print("cluster centers:")
	print(center_xy)
	print(cluster)
	net.calcuRealCenters(center_xy)


# for i in range(node_num):
# 	for c_i in range(cls_num):


if __name__ == '__main__':
	main()
