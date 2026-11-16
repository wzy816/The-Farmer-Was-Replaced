from util import *

 

def f1():
	till_to_soil()
	plant(Entities.Cactus)

# bubble sort with swap and move
def row_sort(x0,y0,x1):
	for x in range(x0,x1-1):
		moved = False
		move_to(x0,y0)
		for _ in range(x1-1-x):
			if measure() > measure(East):
				swap(East)
				moved = True
			move(East)
		if not moved:
			break

def column_sort(x0,y0,y1):
	for y in range(y0,y1-1):
		moved = False
		move_to(x0,y0)
		for _ in range(y1-1-y):
			if measure() > measure(North):
				swap(North)
				moved = True
			move(North)
		if not moved:
			break

clear()

while True:
	ws = WORLD_SIZE

	start_ts = get_time()

	loop(f1,0,0,ws,ws)

	for y in range(0,ws):
		row_sort(0,y,ws)

	for x in range(0,ws):
		column_sort(x,0,ws)
	
	do_harvest_water()

	time_elapsed = get_time() - start_ts
	print("Time elapsed:", time_elapsed)

