# 成就：妙手回春
clear()
set_world_size(8)
from util import *

move_to(0, 0)


def f1():
	till_to_soil()
	plant(Entities.Tree)
	do_fertilizer()


def f2():
	use_item(Items.Weird_Substance)


loop(f1, 0, 0, WORLD_SIZE, WORLD_SIZE)
loop(f2, 0, 0, WORLD_SIZE, WORLD_SIZE)
