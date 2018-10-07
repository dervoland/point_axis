# python 3
# coding=utf-8

import colorsys
from binary_tree import BinaryTree

class BinaryTreePainter:
	# using HSV color space
	# h - is variable
	s = 0.9
	v = 1.

	def make_point_colors__(self, cluster, h1, h2, out_point_colors):
		if cluster is not None:
			#assert(cluster is instance(BinaryTree))
			if cluster.is_leaf():
				out_point_colors[cluster.get_center()] = colorsys.hsv_to_rgb(0.5 * (h1 + h2), self.s, self.v)
			else:
				h_mid = 0.5 * (h1 + h2)
				left_h1, left_h2 = h1, h_mid
				righ_h1, right_h2 = h_mid, h2
				self.make_point_colors__(cluster.get_left_subtree(), left_h1, left_h2, out_point_colors)
				self.make_point_colors__(cluster.get_right_subtree(), righ_h1, right_h2, out_point_colors)
			
	def make_point_colors(self, cluster):
		colors = dict()
		h1, h2 = 0., 1.
		self.make_point_colors__(cluster, h1, h2, colors)
		return colors
