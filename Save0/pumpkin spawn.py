from util import *

# 成就：南瓜大师


def row_plant_pumpkin():
	not_harvested = []
	y = get_pos_y()
	for _ in range(WORLD_SIZE):
		x = get_pos_x()
		till_to_soil()
		plant(Entities.Pumpkin)
		not_harvested.append((x, y))
		move(East)

	while len(not_harvested) > 0:
		next_not_harvested = []
		for x, y in not_harvested:
			move_to(x, y)
			if can_harvest():
				do_water()
			else:
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
				next_not_harvested.append((x, y))

		not_harvested = next_not_harvested


clear()
while True:
	row_spawn_and_wait_all(row_plant_pumpkin)

	must_harvest()
