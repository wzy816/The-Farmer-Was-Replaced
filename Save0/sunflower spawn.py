from util import *


# 成就：向日葵大师
def f():
	while True:
		for _ in range(WORLD_SIZE):
			must_harvest_water()
			till_to_soil()
			plant(Entities.Sunflower)
			move(East)


clear()
move_to(0, 0)
for _ in range(WORLD_SIZE - 1):
	spawn_drone(f)
	move(North)
f()
move(North)
