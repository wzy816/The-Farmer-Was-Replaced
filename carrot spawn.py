from util import *

# 胡萝卜大师

comp = {}
carrot = {}

def update_comp(x,y):
	global comp
	global carrot

	if (x,y) in carrot:
		cxy = carrot.pop((x,y))
		if cxy in comp:
			comp.pop(cxy)

	# 每次 harvest 后 companion 会变
	c = get_companion()
	if c == None:
		return
	
	pt,(cx,cy) = c

	if (cx,cy) not in comp:
		comp[(cx,cy)] = pt
		carrot[(x,y)] = (cx,cy)


def p(plant_type):
	if plant_type == Entities.Carrot:
		till_to_soil()
	plant(plant_type)  
	do_water()

def f():
	global comp

	y = get_pos_y()
	while True:
		for x in range(WORLD_SIZE):

			harvest()

			if (x,y) in comp:
				pt = comp[(x,y)]
				p(pt)

			else:
				p(Entities.Carrot)
				update_comp(x,y)

			move(East)

clear()
row_spawn(f)