# 成就：农业竞争

# while num_items(Items.Hay) < 100000000:
# 	harvest()
# 	move(North)

s = range(get_world_size())

comp = {}
grass = {}


def update_comp(x, y):
	global comp
	global grass

	if (x, y) in grass:
		cxy = grass.pop((x, y))
		if cxy in comp:
			comp.pop(cxy)

	pt, (cx, cy) = get_companion()

	if (cx, cy) not in comp:
		comp[(cx, cy)] = pt
		grass[(x, y)] = (cx, cy)


for x in s:
	for y in s:
		till()
		move(North)
	move(East)

while num_items(Items.Hay) < 100000000:
	for x in s:
		for y in s:
			harvest()

			if (x, y) in comp:
				pt = comp[(x, y)]
				plant(pt)
			else:
				plant(Entities.Grass)
				update_comp(x, y)

			move(North)
		move(East)
