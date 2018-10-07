# python 3
# coding=utf-8


from numpy import linspace


from misc import rnd, permutations
from geometry import Point


def make_random_coodinate(min, max):
	return rnd() * (max - min) + min

def make_random_point(x_min, x_max, y_min, y_max):
	return Point(make_random_coodinate(x_min, x_max), make_random_coodinate(y_min, y_max))

def make_random_points(x_min, x_max, y_min, y_max, count):
	return [make_random_point(x_min, x_max, y_min, y_max) for i in range(0, count)]
	
def make_random_points_around_point(x,y,r,n):
	return [Point(x - 0.5 * r + rnd() * r, y - 0.5 * r + rnd() * r) for i in range(0,n)]
	
def make_rnadom_color():
	return (rnd(), rnd(), rnd())

#def make_interpolate_color_chanal(min, max, n):
#	return np.linspace(min, max, n)
#
#def make_interpolate_color(a, b, n):
#	return list(zip(
#	np.linspace(a[0], b[0], n),
#	np.linspace(a[1], b[1], n),
#	np.linspace(a[2], b[2], n)))

	
def make_random_colors(count):
	return [make_rnadom_color() for i in range(0, count)]
	
def add_points(src, dist):
	for p in src:
		dist.append(p)


def generate_points(count):
	x_min = 0.
	x_max = 200.
	y_min = 0.
	y_max = 200.
	
	init_point_count = count
	
	points = make_random_points(x_min, x_max, y_min, y_max, init_point_count)
	spot_size = 20
	points_row_n = 3
	points_column_n = 4
	points_in_spot = 0
	for x in linspace(spot_size,x_max - spot_size, points_row_n):
		for y in linspace(spot_size,y_max - spot_size, points_column_n):
			add_points(make_random_points_around_point(x, y, spot_size, points_in_spot), points)
	return points

