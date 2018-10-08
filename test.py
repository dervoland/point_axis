# python 3
# coding=utf-8

##############################################
#
# define point placement as type
# point generation
# points serialization
# placement estimation
# find best placement
# visualization
##############################################

import sys
import matplotlib.pyplot as plt
import math
import numpy as np
import time


from binary_tree import BinaryTree
import binary_tree_algo as tree_algo

from generator import generate_points

import geometry
from geometry import Point

import estimator

from representation import draw_binary_tree
	
import binary_tree_creation as btc
from tree_colorization import BinaryTreePainter
	


	
def make_point_numbers(points):
	return {p:i for i,p in enumerate(points)}

def show_tree(tree : BinaryTree, point_numbers):
	painter = BinaryTreePainter()
	color_map = painter.make_point_colors(tree)
	draw_binary_tree(tree, point_numbers, color_map)
	
def create_point_placement_by_bsp(points):
	tree_builder = btc.BSPTreeBuilder()
	tree = tree_builder.make_tree(points)
	tree_algo.minimize_distance_between_subtree_leafs(tree, geometry.quad_euclidean_distance)
	tree_algo.turn_tree_to_order_left_and_right_leafs_by_x(tree)
	oredered_points = list(tree_algo.iterate_leaf_from_left_to_right(tree))
	point_numbers = make_point_numbers(oredered_points)
	#print ("BSP tree:\n", tree)
	#show_tree(tree, point_numbers)
	
	
def create_point_placement_by_clustering(points):
	distance_between_clusters = btc.DistanceBetweenClusterCenters(geometry.quad_euclidean_distance)
	clusterizer = btc.HierarchicalClusterBuilder(distance_between_clusters)
	tree = clusterizer.make_tree(points)
	tree_algo.minimize_distance_between_subtree_leafs(tree, geometry.quad_euclidean_distance)
	tree_algo.turn_tree_to_order_left_and_right_leafs_by_x(tree)
	oredered_points = list(tree_algo.iterate_leaf_from_left_to_right(tree))
	point_numbers = make_point_numbers(oredered_points)
	#print("Cluster tree:\n", tree)
	#show_tree(tree, point_numbers)
	
	
def binary_tree_test():
	# TODO: check empty point collection and one point collection
	point_count = 1000
	print ('Point count = ', point_count)
	points = generate_points(point_count)
	
	# find best point placement
	errors_counter = estimator.DiscontinuityErrorCounter(geometry.euclidean_distance)
	#min_error_count = estimator.find_few_errors_point_permutation(points, errors_counter)
	#print ("Best posible score:", min_error_count)
	
	plt.subplot(211)
	print("Starting...")
	start = time.time()
	cluster_ordered_points = create_point_placement_by_clustering(points)
	print("Finished. Spended time = ", time.time() - start)
	
	plt.subplot(212)
	print("Starting...")
	start = time.time()
	bsp_ordered_points = create_point_placement_by_bsp(points)
	print("Finished. Spended time = ", time.time() - start)
	
	# estimate point placement
	#print ("Cluster score: ", errors_counter(cluster_ordered_points))
	#print ("Bsp score: ", errors_counter(bsp_ordered_points))
		
	#plt.show()

def main():
	binary_tree_test()
	
if __name__ == "__main__":
	main()