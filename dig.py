from util import *
def dig_until_clay():
	while get_ground_type() != Grounds.Clay:
		dig()
		
clear()

row_spawn_and_wait_all(to_row_f(dig_until_clay))