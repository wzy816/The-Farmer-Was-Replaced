from util import *


# 胡萝卜 demo
def f1():
	till_to_soil()
	plant(Entities.Carrot)


def f2():
	if do_harvest_water():
		plant(Entities.Carrot)


clear()
loop(f1, 0, 0, WORLD_SIZE, WORLD_SIZE)
while True:
	loop(f2, 0, 0, WORLD_SIZE, WORLD_SIZE)
