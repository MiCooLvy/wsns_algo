#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : kmeans.py
# @Software: PyCharm
# @Author: Kenn
# @Date  : 2018/4/3
# @Desc  :
from WsnsToplogy import WsnsToplogy
import numpy as np
from sklearn.cluster import KMeans


def main():
	node_num = 300
	monit_area = [200, 200]
	net = WsnsToplogy(monit_area = monit_area, node_num = node_num)
	# print(net.getNode_XY())
	nodes_xy = net.getNode_XY()
	cls_num = int(np.ceil(np.sqrt(node_num / 2)))  # 上取整
	print("cluster number: " + str(cls_num))
	clusterer = KMeans(n_clusters = cls_num, max_iter = 520, random_state = 32)
	kmeans = clusterer.fit(nodes_xy)
	center_xy = kmeans.cluster_centers_
	cluster = kmeans.labels_
	print("cluster centers:")
	print(center_xy)
	print(cluster)
	real_idx = np.zeros(len(center_xy))
	for i in range(len(center_xy)):
		real_idx[i] = net.calcuRealCenters(center_xy[i])
	print(real_idx)
	net.drawAllNodes()
	net.drawClusterTopo(real_idx, cluster)
	net.show()


if __name__ == '__main__':
	main()
