from util import *

# 向日葵 demo


def f1(x, y):
	till_to_soil()
	plant(Entities.Sunflower)
	pedal[measure()].append((x, y))


clear()
while True:

	pedal = {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
	loop2(f1, 0, 0, WORLD_SIZE, WORLD_SIZE)

	for i in range(15, 6, -1):
		harvested = 0
		max_harvest = len(pedal[i])
		while harvested < max_harvest:
			for x, y in pedal[i]:
				move_to(x, y)
				if do_harvest_water():
					harvested += 1
