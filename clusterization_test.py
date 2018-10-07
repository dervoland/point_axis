1# python 3
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
#import colorsys

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

def create_point_placement_by_bsp(points):
	tree_builder = btc.BSPTreeBuilder()
	tree = tree_builder.make_tree(points)
	
def create_point_placement_by_clustering(points):
	distance_between_clusters = btc.DistanceBetweenClusterCenters(geometry.quad_euclidean_distance)
	clusterizer = btc.HierarchicalClusterBuilder(distance_between_clusters)
	tree = clusterizer.make_tree(points)
	tree_algo.minimize_distance_between_subtree_leafs(tree, geometry.quad_euclidean_distance)
	tree_algo.turn_tree_to_order_left_and_right_leafs_by_x(tree)
	print("Cluster tree:\n", tree)
	painter = BinaryTreePainter()
	color_map = painter.make_point_colors(tree)
	point_number = make_point_numbers(points)
	draw_binary_tree(tree, point_number, color_map)
	return list(tree_algo.iterate_leaf_from_left_to_right(tree))
	
	
def binary_tree_test():
	# TODO: check empty point collection and one point collection
	points = generate_points(4)
	
	# find best point placement
	#errors_counter = estimator.DiscontinuityErrorCounter(geometry.euclidean_distance)
	#min_error_count = estimator.find_few_errors_point_permutation(points, errors_counter)
	#print ("Best posible score:", min_error_count)
	#plt.subplot(211)
	
	#plt.subplot(212)
	#ordered_points = create_point_placement_by_clustering(points)
	
	# estimate point placement
	#current_error_count = errors_counter(ordered_points)
	#print ("Score: ", current_error_count)
	
	# bsp
	create_point_placement_by_bsp(points)
	
	
	
	
	#plt.subplot(212)
	#present_manhattan_distance_cluster(points)
	
	#plt.subplot(212)
	#present_nearest_euclidean_distance_cluster(points)
	
	plt.show()

def main():
	binary_tree_test()
	
if __name__ == "__main__":
	main()