from util import *

# 成就：干草大师

companion = {}


def hw():
	if can_harvest():
		harvest()
		use_item(Items.Water)


def p(plant_type):
	if plant_type == Entities.Carrot:
		till_to_soil()
	plant(plant_type)


def f():
	global companion

	while True:
		for _ in range(WORLD_SIZE):
			hw()

			x, y = get_pos_x(), get_pos_y()

			if (x, y) in companion:
				p(companion[(x, y)])
			else:
				c = get_companion()
				if c != None:
					pt, (cx, cy) = c
					companion[(cx, cy)] = pt

			move(East)


clear()
move_to(0, 0)
for i in range(WORLD_SIZE):
	if not spawn_drone(f):
		f()
	move(North)
