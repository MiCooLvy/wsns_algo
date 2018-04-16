#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : WsnsToplogy.py
# @Software: PyCharm
# @Author: Kenn
# @Date  : 2018/4/3
# @Desc  :
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class WsnsToplogy():
	def __init__(self, monit_area, node_num=0, init_engy=1.0):
		"""
		初始化函数
		:param monit_area: 检测区域范围。1x2的列表，如 [100,100]
		:param node_num: 网络总的节点个数。
		:param init_engy: 初始化能量
		"""
		# 设置随机种子可以保持运行结果的一致
		np.random.seed(4)
		# 设置坐标轴字体
		mpl.rcParams['xtick.labelsize'] = 16
		mpl.rcParams['ytick.labelsize'] = 16
		fig = plt.figure('Toplogy')
		self.__ax = fig.add_subplot(1, 1, 1)

		# 无线传感网基本参数
		self.__Eetec = 50e-9
		self.__Efs = 10e-12
		self.__Emp = 0.0013e-12
		self.__EDA = 5e-9
		self.__packetSize = 2000
		self.__baseStation = []

		self.__monit_area = monit_area
		self.__node_num = node_num
		self.__init_engy = [init_engy] * node_num
		self.__node_alive = np.ones(self.__node_num)
		print(self.__node_alive)
		# 随机分布节点
		self.__node_xy = self.__dstrTop()

	def __dstrTop(self):
		"""
		私有化方法，负责生成节点坐标
		"""
		# 随机生成节点坐标
		node_xy = [0, 0]
		node_xy[0] = np.random.rand(self.__node_num) * self.__monit_area[0]
		node_xy[1] = np.random.rand(self.__node_num) * self.__monit_area[1]
		return np.transpose(node_xy)

	########################
	def calcuAliveNodesNum(self):
		return np.sum(self.__node_alive == 1)

	def calcuCenter(self):
		"""
		计算网络中心点
		:return:
		"""
		return [np.mean(self.__node_xy[0]), np.mean(self.__node_xy[1])]

	def calcDist(self, node1, node2):
		"""
		计算两点间的距离的平方
		:param node1:
		:param node2:
		:return: 距离的平方
		"""
		return np.sum(np.square(np.array(node1) - np.array(node2)))

	def calcCRadius(self):
		"""
		计算中心圆的半径
		:return:
		"""
		sum = 0
		C = self.calcuCenter()
		for i in range(self.__node_num):
			sum += np.sqrt(self.calcDist(C, [self.__node_xy[0][i], self.__node_xy[1][i]]))
		return sum / self.__node_num

	#  寻找实际类中心点
	def calcuRealCenters(self, cluster_centers):
		m, n = np.shape(cluster_centers)
		for i in range(self.__node_num):
			for j in range(m):
				pass

			# TODO：寻找实际点

	###################
	def drawDot(self, x, y, color='r'):
		"""
		画点
		:param x:
		:param y:
		:param color:
		"""
		plt.scatter(x, y, c = color)
		plt.savefig('top.png')

	def drawCircle(self, x, y, r, color='g'):
		cir = plt.Circle(xy = (x, y), radius = r, color = color, fill = False)
		self.__ax.add_patch(cir)
		plt.savefig('top.png')

	def drawAllNodes(self):
		"""
		画所有节点
		"""
		plt.scatter(self.__node_xy[0], self.__node_xy[1])
		plt.savefig('top.png')

	def show(self):
		"""
		显示图
		"""
		plt.show()

	################
	def getOneNode_XY(self, index):
		"""
		获取一个节点坐标
		:param index: 节点索引
		:return: 一个节点坐标
		"""
		return [self.__node_xy[0][index], self.__node_xy[1][index]]

	def getMonitArea(self):
		"""
		获取监测区域
		:return:  1x2 list
		"""
		return self.__monit_area

	def getNodeNum(self):
		"""
		获取节点数量
		:return: 数量
		"""
		return self.__node_num

	def getInitEngy(self):
		"""
		获取初始能量
		:return: 初始能量
		"""
		return self.__init_engy

	def getNode_XY(self):
		"""
		获取所有节点坐标
		:return: list
		"""
		return self.__node_xy

	def getEetec(self):
		return self.__Eetec

	def setEetec(self, val):
		self.__Eetec = val

	def getEfs(self):
		return self.__Efs

	def setEfs(self, val):
		self.__Efs = val

	def getEmp(self):
		return self.__Emp

	def setEmp(self, val):
		self.__Emp = val

	def getEDA(self):
		return self.__EDA

	def setEDA(self, val):
		self.__EDA = val

	def getPkSize(self):
		return self.__packetSize

	def setPkSize(self, val):
		self.__packetSize = val

	def getBS_XY(self):
		return self.__baseStation

	def setBS_XY(self, coor):
		self.__baseStation = coor
