from util import *

# 树 demo


def f1(x, y):
	# 棋盘式
	if (x + y) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)


def f2(x, y):
	if do_harvest_water():
		f1(x, y)


clear()
loop2(f1, 0, 0, WORLD_SIZE, WORLD_SIZE)
while True:
	loop2(f2, 0, 0, WORLD_SIZE, WORLD_SIZE)
