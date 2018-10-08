# python 3
# coding=utf-8

import sys
import geometry
from geometry import Point
from binary_tree import BinaryTree
from geometry import euclidean_distance

##################################################################
# Clustering
##################################################################
class DistanceBetweenClusterCenters:
	ditance_fun = None
	
	def __init__(self, ditance_fun = euclidean_distance):
		self.ditance_fun = ditance_fun
		
	def __call__(self, cluster_a, cluster_b):
		assert(isinstance(cluster_a, BinaryTree))
		assert(isinstance(cluster_b, BinaryTree))
		return self.ditance_fun(cluster_a.get_center(), cluster_b.get_center())


class MinDistanceBetweenClustersPoints:
	ditance_fun = None
	
	def __init__(self, ditance_fun = euclidean_distance):
		self.ditance_fun = ditance_fun
		
	def nearest_euclidean_distance_between_clusters(self, cluster_a, cluster_b):
		assert(isinstance(cluster_a, BinaryTree))
		assert(isinstance(cluster_b, BinaryTree))
		min_d = sys.float_info.max
		for pointA in iterate_leaf_from_left_to_right(cluster_a):
			for pointB in iterate_leaf_from_left_to_right(cluster_b):
				d = self.ditance_fun(pointA, pointB)
				if d < min_d:
					min_d = d
		return min_d
	
	def __call__(self, cluster_a, cluster_b):
		return self.nearest_euclidean_distance_between_clusters(cluster_a, cluster_b)


class HierarchicalClusterBuilder:
	distance_between_clusters_fun = None

	def __init__(self, distance_between_clusters_fun = DistanceBetweenClusterCenters):
		self.distance_between_clusters_fun = distance_between_clusters_fun
	
	def make_simple_clusters(self, points):
		return [BinaryTree.make_leaf(p) for p in points]
		
	def find_nearest_clusters(self, clusters):
		if (len(clusters) == 2):
			return 0,1
		n = len(clusters)
		min_d = sys.float_info.max
		i_ = 0
		j_ = 0
		for i in range(0, n):
			for j in range(i+1, n):
				d = self.distance_between_clusters_fun(clusters[i], clusters[j])
				if d < min_d: 
					min_d = d
					i_ = i
					j_ = j
		return i_, j_

	def unite_nearest_clusters(self, clusters):
		if (len(clusters) < 2):
			return
		i,j = self.find_nearest_clusters(clusters)
		new_cluster = BinaryTree.make_supertree(clusters[i], clusters[j])
		del clusters[max(i,j)]
		del clusters[min(i,j)]
		clusters.append(new_cluster)

	def make_binary_tree(self, clusters):
		root = None
		while len(clusters) > 1:
			self.unite_nearest_clusters(clusters)
			root = clusters[0]
		return root
		
	def make_tree(self, points):
		clusters = self.make_simple_clusters(points)
		return self.make_binary_tree(clusters)
		
		
##################################################################
# BSP 
##################################################################
class BSPTreeBuilder:
	
	#def __init__(self):
	
	def calculate_gabarit(self, points):
		x_arr = Point.get_x(points)
		y_arr = Point.get_y(points)
		return min(x_arr), max(x_arr), min(y_arr), max(y_arr)
		
	def split_points(self, points, pred):
		left, right = [],[]
		for p in points:
			if pred(p):
				left.append(p)
			else:
				right.append(p)
		return left, right
		
	def split_space_by_lager_gabarit_size(self, points):
		x_min, x_max, y_min, y_max = self.calculate_gabarit(points)
		dx, dy = abs(x_max - x_min), abs(y_max - y_min)
		assert(dx > 0 or dy > 0) # may be not unique points
		if dx > dy:
			x_mid = 0.5 * (x_max + x_min)
			return self.split_points(points, (lambda p : p.x < x_mid))
		else:
			y_mid = 0.5 * (y_max + y_min)
			return self.split_points(points, (lambda p : p.y < y_mid))
	
	def make_tree(self, points):
		if len(points) > 0:
			if len(points) == 1:
				return BinaryTree.make_leaf(points[0])
			else:
				left_points, right_points = self.split_space_by_lager_gabarit_size(points)
				assert(len(left_points) > 0)
				assert(len(right_points) > 0)
				left_tree = self.make_tree(left_points)
				right_tree = self.make_tree(right_points)
				return BinaryTree.make_supertree(left_tree, right_tree)
		else:
			return None
		
			