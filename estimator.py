# python 3
# coding=utf-8

import sys

import misc
from geometry import quad_euclidean_distance

####################################################
# All estimations are divided onto
# 'errors coiunting'
# and 
# 'quality estimation'.
# The solution is betted when 'errors counter' returns minimal value (0 is perfect).
# The 'quality estimation' returns normalized value in range (0,1].
# The solution is betted when 'quality estimation' returns maximun value (1 is perfect).
####################################################

####################################################
# DiscontinuityErrorCounter
####################################################
class DiscontinuityErrorCounter:
	distance_fun = None
	
	def __init__(self, distance_fun):
		self.distance_fun = distance_fun
		
	def __call__(self, points):
		return self.count_discontinuity(points)
		
	
	def count_discontinuity__no_check(self, less_oredered_distances):
		discontinuity_count = 0
		for i in range(0, len(less_oredered_distances)):
			for j in  range(i+1, len(less_oredered_distances)):
				if less_oredered_distances[i] > less_oredered_distances[j]:
					discontinuity_count += 1
		return discontinuity_count
		
	def count_discontinuity_around_base_index(self, points, base_index):
		base_p = points[base_index]
		left_distances = [self.distance_fun(base_p, p) for p in reversed(points[:base_index])]
		right_distances = [self.distance_fun(base_p, p) for p in points[base_index+1:]]
		return self.count_discontinuity__no_check(left_distances) + self.count_discontinuity__no_check(right_distances)
	
	def count_discontinuity(self, points):
		count = 0
		for i in range(0, len(points)):
			count += self.count_discontinuity_around_base_index(points, i)
		return count

####################################################
#def get_summary_distance_between_neighbor_points(points, distance_fun):
#	d = 0
#	n = len(points)
#	if n > 1:
#		for i in range(1, n):
#			d += distance_fun(points[i-1], points[i])
#	return d
#
#def calculate_gabarit_diagonal(points):
#	x_values = get_x(points)
#	y_values = get_y(points)
#	left_bottom = Point(min(x_values), min(y_values))
#	right_top = Point(max(x_values), max(y_values))
#	return left_bottom, right_top
#	
#def get_best_possible_distance(points, distance_fun):
#	p0, p1 = calculate_gabarit_diagonal(points)
#	return distance_fun(p0,p1)
#	
#def estimate_point_placement(points, distance_fun):
#	sum_dist = get_summary_distance_between_neighbor_points(points, distance_fun)
#	if 0 == sum_dist:
#		return 1
#	else:
#		best_dist = get_best_possible_distance(points, distance_fun)
#		return best_dist / sum_dist


		
####################################################
def find_few_errors_point_permutation(points, error_counter):
	min_errors = 0
	for point_placement in misc.permutations(points):
		err_count = error_counter(point_placement)
		if err_count < min_errors:
			min_errors = err_count
	return min_errors

def find_best_quality_point_permutation(points, quality_estimator):
	best_score = sys.maxsize
	for point_placement in misc.permutations(points):
		score = quality_estimator(point_placement)
		if score > best_score:
			best_score = score
	return best_score
