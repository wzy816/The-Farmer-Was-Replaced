from util import *


def plant_rice_row():
	# exploit all clay unti all rock
	while True:
		not_clay = 0
		
		for _ in range(WORLD_SIZE):
			
			# grow cycle
			if can_harvest():
				harvest()
			elif get_ground_type() == Grounds.Clay:
				plant(Entities.Rice)
			elif get_ground_type() == Grounds.Dry_Rice_Terrace:
				dig()
			else:
				not_clay += 1
			move(East)

		if not_clay >= WORLD_SIZE:
			break
	
def plant_rice():
	dig_all_until(Grounds.Clay)
	row_spawn_and_wait_all(to_row_f(plant_rice_row))
	

plant_rice()