set_world_size(5)
from util import *


# 成就：迷宫大师、黄金大亨
def gen_maze():
	global substance
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance)


def f():
	global substance
	cnt = 0
	while True:
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, substance)
			cnt += 1

		if cnt > 200:
			harvest()
			gen_maze()
			cnt = 0


substance = WORLD_SIZE * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

for i in range(5):
	for j in range(5):
		move_to(i, j)
		spawn_drone(f)

gen_maze()
