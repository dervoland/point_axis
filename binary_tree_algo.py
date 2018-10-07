# python 3
# coding=utf-8

from binary_tree import BinaryTree


def iterate_leaf_from_left_to_right(tree):
	if tree is not None:
		assert(isinstance(tree, BinaryTree))
		if tree.is_leaf():
			yield tree.get_center()
		else:
			for p in iterate_leaf_from_left_to_right(tree.get_left_subtree()):
				yield p
			for p in iterate_leaf_from_left_to_right(tree.get_right_subtree()):
				yield p


def turn_tree(tree):
	if tree is not None:
		assert(isinstance(tree, BinaryTree))
		tree.swap_left_and_right_subtrees()
		turn_tree(tree.get_left_subtree())
		turn_tree(tree.get_right_subtree())

def find_right_leaf(tree):
	if tree is not None:
		assert(isinstance(tree, BinaryTree))
		if tree.is_leaf():
			return tree
		else:
			return find_right_leaf(tree.get_right_subtree())
	else:
		return None
		
def find_left_leaf(tree):
	if tree is not None:
		assert(isinstance(tree, BinaryTree))
		if tree.is_leaf():
			return tree
		else:
			return find_left_leaf(tree.get_left_subtree())
	else:
		return None

# general order would be left-to-right
# normal position is
#    o
#  L/ \R
# L-R L-R
def minimize_distance_between_subtree_leafs(tree, distance_fun):
	if tree is not None:
		assert(isinstance(tree, BinaryTree))
		if not tree.is_leaf():
			left_subtree = tree.get_left_subtree()
			right_subtree = tree.get_right_subtree()
			# call subcluters minimization
			minimize_distance_between_subtree_leafs(left_subtree, distance_fun)
			minimize_distance_between_subtree_leafs(right_subtree, distance_fun)
			# minimize own sub trees
			LL = find_left_leaf(left_subtree)
			LR = find_right_leaf(left_subtree)
			RL = find_left_leaf(right_subtree)
			RR = find_right_leaf(right_subtree)
			LL_RL_dist = distance_fun(LL.get_center(), RL.get_center())
			LL_RR_dist = distance_fun(LL.get_center(), RR.get_center())
			LR_RL_dist = distance_fun(LR.get_center(), RL.get_center())
			LR_RR_dist = distance_fun(LR.get_center(), RR.get_center())
			min_dist = min([LL_RL_dist, LL_RR_dist, LR_RL_dist, LR_RR_dist])
			if (LL_RL_dist == min_dist):
				turn_tree(left_subtree)
			elif (LL_RR_dist == min_dist):
				turn_tree(left_subtree)
				turn_tree(right_subtree)
			elif (LR_RL_dist == min_dist):
				return # do nothing
			elif (LR_RR_dist == min_dist):
				turn_tree(right_subtree)

def turn_tree_to_order_left_and_right_leafs_by_x(tree):
	if tree is not None:
		assert(isinstance(tree, BinaryTree))
		left_leaf_point = find_left_leaf(tree).get_center()
		right_leaf_point = find_right_leaf(tree).get_center()
		if right_leaf_point.x < left_leaf_point.x:
			turn_tree(tree)
