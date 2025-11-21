from util import *

# weird substance demo

clear()


def tree():
	plant(Entities.Tree)
	do_fertilizer()


def bush():
	plant(Entities.Bush)
	do_fertilizer()


def even_f():
	for i in range(WORLD_SIZE):
		if i % 2 == 0:
			tree()
		else:
			bush()
		move(East)


def odd_f():
	for i in range(WORLD_SIZE):
		if i % 2 == 0:
			bush()
		else:
			tree()
		move(East)


while True:
	odd_even_row_spawn_and_wait_all(even_f, odd_f)

	row_spawn_and_wait_all(to_row_f(must_harvest_water))
