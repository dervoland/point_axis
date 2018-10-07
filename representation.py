# python 3
# coding=utf-8

import matplotlib.pyplot as plt
from numpy import linspace

from geometry import Point
from binary_tree import BinaryTree
import binary_tree_algo as tree_algo

def draw_point_numbers(points, point_nuber_markers):
	n = 0
	for p in points:
		plt.text(p.x, p.y, str(point_nuber_markers[p]), color="black", fontsize=10)
		n += 1

def draw_line_segment(p1, p2):
	plt.plot([p1.x, p2.x], [p1.y, p2.y], 'r--', color = "black", linewidth=1.0)
	
def draw_point(p):
	plt.scatter([p.x], [p.y], c = "black", s=10)
	
def draw_line_segments(points):
	plt.plot(Point.get_x(points), Point.get_y(points), color = "black")
	
def draw_binary_tree_points(tree, point_numbers, color_map):
	if tree is not None:
		points = list(tree_algo.iterate_leaf_from_left_to_right(tree))
		colors = [color_map[point]  for point in points]
		plt.scatter(Point.get_x(points), Point.get_y(points), c=colors)
		draw_point_numbers(points, point_numbers)
		draw_point_in_line(points, color_map, point_numbers)
	
def draw_binary_tree_edges(tree):
	if tree is not None:
		if not tree.is_leaf():
			c = tree.get_center()
			draw_point(c)
			if tree.get_left_subtree() is not None:
				draw_line_segment(c, tree.get_left_subtree().get_center())
				draw_binary_tree_edges(tree.get_left_subtree())
			if tree.get_right_subtree() is not None:
				draw_line_segment(c, tree.get_right_subtree().get_center())
				draw_binary_tree_edges(tree.get_right_subtree())

def draw_binary_tree(tree, point_numbers, color_map):
	draw_binary_tree_edges(tree)
	draw_binary_tree_points(tree, point_numbers, color_map)

def draw_point_in_line(points, color_map, point_nuber_markers):
	if len(points) == 0:
		return
	y = -10.
	x_min, x_max = 0, 200
	x_pos = linspace(x_min, x_max,len(points))
	
	colors = [color_map[point]  for point in points]
	plt.scatter(x_pos, [y]*len(points), c=colors)
	
	for i in range(0, len(points)):
		p = points[i]
		plt.text(x_pos[i], y, str(point_nuber_markers[p]), color="black", fontsize=10)
