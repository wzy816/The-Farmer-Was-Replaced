from util import *

# 成就：木材大师


def hw():
	if can_harvest():
		harvest()
		use_item(Items.Water)


def p(plant_type):
	if plant_type == Entities.Carrot:
		till_to_soil()
	plant(plant_type)


def f():
	companion = {}

	while True:
		for _ in range(WORLD_SIZE):
			hw()

			x, y = get_pos_x(), get_pos_y()

			if (x + y) % 2 == 0:
				p(Entities.Tree)
				c = get_companion()
				if c != None:
					pt, (cx, cy) = c
					if (cx + cy) % 2 == 1:
						companion[(cx, cy)] = pt
			else:
				if (x, y) in companion:
					p(companion[(x, y)])
				else:
					p(Entities.Bush)

			move(East)


clear()
move_to(0, 0)
for i in range(WORLD_SIZE):
	if not spawn_drone(f):
		f()
	move(North)
