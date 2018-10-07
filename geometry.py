# python 3
# coding=utf-8

import math


class Point:
	x = float(0.)
	y = float(0.)
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	@classmethod
	def between(point,a,b):
		return point((a.x + b.x) * 0.5, (a.y + b.y) * 0.5)
		
	def __str__(self):
		return "(x={0:.2f} y={1:.2f})".format(self.x, self.y)

	def __repr__(self):
		return str(self)
		
	@staticmethod
	def get_x(points):
		return [point.x for point in points]
	
	@staticmethod
	def get_y(points):
		return [point.y for point in points]


def __manhattan_distance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

def manhattan_distance(a : Point, b : Point):
	assert(isinstance(a, Point))
	assert(isinstance(b, Point))
	return __manhattan_distance(a.x, a.y, b.x, b.y)
	
def __euclidean_distance(x1, y1, x2, y2):
	return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
	
def euclidean_distance(a : Point, b : Point):
	assert(isinstance(a, Point))
	assert(isinstance(b, Point))
	return __euclidean_distance(a.x, a.y, b.x, b.y)

def __quad_euclidean_distance(x1, y1, x2, y2):
	return (x1 - x2)**2 + (y1 - y2)**2
	
def quad_euclidean_distance(a : Point, b : Point):
	assert(isinstance(a, Point))
	assert(isinstance(b, Point))
	return __quad_euclidean_distance(a.x, a.y, b.x, b.y)

