#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ap.py
# @Software: PyCharm
# @Author: Kenn
# @Date  : 2018/4/16
# @Desc  : AffinityPropagation 算法分簇
from WsnsToplogy import WsnsToplogy
import numpy as np
from sklearn.cluster import AffinityPropagation


def main():
	node_num = 300
	area = [200, 200]
	net = WsnsToplogy(monit_area = area, node_num = node_num)
	node_xy = net.getNode_XY()
	cls_num = int(np.ceil(np.sqrt(node_num / 2)))  # 上取整
	ap = AffinityPropagation(preference = -6000, max_iter = 520).fit(node_xy)
	cluster = ap.labels_
	print(cluster)
	center_xy = ap.cluster_centers_
	print(center_xy)
	print(ap.cluster_centers_indices_)
	net.drawAllNodes()
	net.drawClusterTopo(ap.cluster_centers_indices_, cluster)
	net.show()


if __name__ == '__main__':
	main()
