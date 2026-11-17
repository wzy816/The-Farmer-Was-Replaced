from util import *
from heapq import *


def plant_bamboo_row():
	# take 2 rows,

	while True:
		h = []
		
		# plant at 2nd, 1st row empty
		move(North)
		for _ in range(WORLD_SIZE):
			till_to_soil()
			plant(Entities.Bamboo)
			m = measure()
		
			i = (m-0, get_pos_x(), get_pos_y(), m)
			heappush(h,i)
			move(East)
		
		move(South)
		
		wait = 0
		while h:
		
			i = heappop(h)
			hover(i[3])
			move_to(i[1], i[2])
			m = measure()
			move(South)
			if m == i[3]:
				# growing or reach top
				i2 = (i[0]+2,i[1],i[2],i[3])
				wait += 1
			else:
				# fruit picked
				i2 = (m-i[0]+2,i[1],i[2],m)
				wait = 0
				
			heappush(h,i2)
			
			# exit when all reach top
			if wait >= WORLD_SIZE*2:
				break
				
		# harvest all
		hover(1)
		move(North)
		for _ in range(WORLD_SIZE):
			move(East)
	
		move(South)


clear()
for _ in range(HALF_WORLD_SIZE):
	spawn_drone(plant_bamboo_row)
	move(North)
	move(North)
