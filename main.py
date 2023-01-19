import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import random
import copy
from sklearn.datasets import load_iris

def clusterization(array, k):
	n = len(array)
	dim = len(array[0])

	cluster = [[0 for i in range(dim)] for q in range(k)] #двумерный массив размерностью dim * k, содержащий k точек — центры кластеров
	cluster_content = [[] for i in range(k)] #массив, содержащий в себе k массивов — массивов точек принадлежащих соответствующему кластеру

	for i in range(dim):
		for q in range(k):
			cluster[q][i] = random.randint(0, max_cluster_value)# рандомно ставим начальные центры

	cluster_content = data_distribution(array, cluster)

	privious_cluster = copy.deepcopy(cluster)
	while 1:
		cluster = cluster_update(cluster, cluster_content, dim)
		cluster_content = data_distribution(array, cluster)
		if cluster == privious_cluster:
			break
		privious_cluster = copy.deepcopy(cluster)

	visualisation_2d(cluster_content,cluster)#визуализация 2-мерная обычно всё понятно
	visualisation_3d(cluster_content,cluster)#визуализация 3-мерная включать когда вщ ничего не понятно

def data_distribution(array, cluster):
    cluster_content = [[] for i in range(k)]

    for i in range(n):
        min_distance = float('inf')# За начальное кратчайшее расстояние (min_distance) берётся несоизмеримо большое со значениями точек число;
        situable_cluster = -1
        for j in range(k):
            distance = 0
            for q in range(dim): #Затем происходит вычисление расстояния до центра каждого кластера;
                distance += (array[i][q] - cluster[j][q]) ** 2

            distance = distance ** (1 / 2)
            if distance < min_distance: #Если вычисленное расстояние меньше минимального, то минимальное расстояние приравнивается к вычисленному и точка привязывается к этому кластеру (situable_cluster);
                min_distance = distance
                situable_cluster = j

        cluster_content[situable_cluster].append(array[i])#После обработки точки, в массив cluster_content в выбранный кластер (situable_cluster) кластер вкладывается значение точки.

    return cluster_content

def cluster_update(cluster, cluster_content, dim): #После распределения точек по центрам кластеров происходит перераспределение уже центров кластеров по привязанным к ним точкам
	k = len(cluster)
	for i in range(k): #по i кластерам
		for q in range(dim): #по q параметрам
			updated_parameter = 0
			for j in range(len(cluster_content[i])):
				updated_parameter += cluster_content[i][j][q]
			if len(cluster_content[i]) != 0:
				updated_parameter = updated_parameter / len(cluster_content[i])
			cluster[i][q] = updated_parameter
	return cluster

def visualisation_2d(cluster_content,cluster):

	k = len(cluster_content)
	plt.grid()
	plt.xlabel("x")
	plt.ylabel("y")

	for i in range(k):
		x_coordinates = []
		y_coordinates = []
		for q in range(len(cluster_content[i])):
			x_coordinates.append(cluster_content[i][q][0])
			y_coordinates.append(cluster_content[i][q][1])
		plt.scatter(x_coordinates, y_coordinates, cmap = "rainbow")

	m = len(cluster)
	for i in range(m):  # расставляем центры кластеров
		x_center = []
		y_center = []
		for q in range(len(cluster[i])):
			x_center.append(cluster[i][0])
			y_center.append(cluster[i][1])
		plt.scatter(x_center, y_center, marker="+",cmap = "rainbow", c = "black")
	plt.show()


def visualisation_3d(cluster_content,cluster):
	ax = plt.axes(projection="3d")
	plt.xlabel("x")
	plt.ylabel("y")

	k = len(cluster_content)

	for i in range(k):# расставляем точки
		x_coordinates = []
		y_coordinates = []
		z_coordinates = []
		for q in range(len(cluster_content[i])):
			x_coordinates.append(cluster_content[i][q][0])
			y_coordinates.append(cluster_content[i][q][1])
			z_coordinates.append(cluster_content[i][q][2])
		ax.scatter(x_coordinates, y_coordinates, z_coordinates,cmap = "rainbow")

	m = len(cluster)
	for i in range(m):#расставляем центры кластеров
		x_center = []
		y_center = []
		z_center = []
		for q in range(len(cluster[i])):
			x_center.append(cluster[i][0])
			y_center.append(cluster[i][1])
			z_center.append(cluster[i][2])
		ax.scatter(x_center, y_center, z_center, marker = "+", cmap = "rainbow",c = "black")
	plt.show()
###############################################################################################
max_cluster_value = 5
k = 6
obj = load_iris()
array = obj.data
n = len(array)
dim = len(array[0])
clusterization(array, k)