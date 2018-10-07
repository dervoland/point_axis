# python 3
# coding=utf-8

from geometry import Point

class BinaryTree:
	center = Point(0.,0.)
	left_subtree = None
	right_subtree = None
	
	def get_center(self):
		return self.center
		
	def get_left_subtree(self):
		return self.left_subtree
		
	def get_right_subtree(self):
		return self.right_subtree
		
	def is_leaf(self):
		return (self.get_left_subtree() is None) and (self.get_right_subtree() is None)
	
	def swap_left_and_right_subtrees(self):
		self.left_subtree, self.right_subtree = self.right_subtree, self.left_subtree
			
	def __init__(self, point, left_subtree, right_subtree):
		self.center = point
		self.left_subtree = left_subtree
		self.right_subtree = right_subtree
	
	@classmethod
	def make_leaf(tree, point):
		return tree(point, None, None)
		
	@classmethod
	def make_supertree(tree, left_subtree, right_subtree):
		assert(left_subtree is not None)
		assert(right_subtree is not None)
		center = Point.between(left_subtree.get_center(), right_subtree.get_center())
		return tree(center, left_subtree, right_subtree)
		
	def __str__(self):
		if (self.is_leaf()):
			ret = "LEAF" + str(self.get_center())
		else:
			ret = "CENTER" + str(self.get_center())
			ret += "L:" + str(self.get_left_subtree())
			ret += "R:" + str(self.get_right_subtree())
		return "[" + ret + "]"
	
	def __repr__(self):
		return str(self)
