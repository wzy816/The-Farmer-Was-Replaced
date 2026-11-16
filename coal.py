from util import *
from heapq import *

def d0(target_z):
	def f():
		while get_pos_z() >= target_z and get_ground_type() != Grounds.Coal:
			dig()
	return f

def d1(target_z):
	def f():
		while get_pos_z() >= target_z:
			dig()
	return f

def m0():
	if get_pos_z() > z:
		return get_pos_z()

clear()
spacing = 8
z = -4
while z > -100:
	
	# dig to z
	spacing_spawn_and_wait_all(d0(z), spacing)
	
	# peak shallower depths = coal zs
	zs = set(spacing_loop(m0,spacing))

	if len(zs) >0:
		zs = reverse(sort(list(zs)))
		print(zs)
		for _z in zs:
			grid_spawn_and_wait_all(d1(_z))
			
	# dig all above z
	grid_spawn_and_wait_all(d1(z))

	z -= 4
	
