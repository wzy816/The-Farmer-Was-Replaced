# plant, harvest, water

def do_water():
	w = get_water()
	for _ in range(4-4*w):
		use_item(Items.Water)

def do_harvest():
	if can_harvest():
		harvest()
		return True
	return False

def do_harvest_water():
	is_h = do_harvest()
	do_water()
	return is_h

def do_fertilizer():
	use_item(Items.Fertilizer)

def must_harvest_water():
	while True:
		if can_harvest():
			harvest()
			break
	do_water()

def must_harvest():
	while True:
		if can_harvest():
			harvest()
			break

def till_to_soil():
	if get_ground_type() != Grounds.Soil:
		till()


def till_to_grassland():
	if get_ground_type() != Grounds.Grassland:
		till()

# move

def move_east_n(n):
	for _ in range(n):
		move(East)

def move_west_n(n):
	for _ in range(n):
		move(West)

def move_south_n(n):
	for _ in range(n):
		move(South)

def move_north_n(n):
	for _ in range(n):
		move(North)

WORLD_SIZE = get_world_size()
HALF_WORLD_SIZE = WORLD_SIZE // 2
WORLD_SIZE_SQ = WORLD_SIZE * WORLD_SIZE

def move_to(x, y, cross_boundary=True):
	dx = x - get_pos_x()
	if dx>0:
		if dx <= HALF_WORLD_SIZE or not cross_boundary:
			move_east_n(dx)
		else:
			move_west_n(WORLD_SIZE - dx)
	else:
		if -dx <= HALF_WORLD_SIZE or not cross_boundary:
			move_west_n(-dx)
		else:
			move_east_n(WORLD_SIZE + dx)

	dy = y - get_pos_y()
	if dy>0:
		if dy <= HALF_WORLD_SIZE or not cross_boundary:
			move_north_n(dy)
		else:
			move_south_n(WORLD_SIZE - dy)
	else:
		if -dy <= HALF_WORLD_SIZE or not cross_boundary:
			move_south_n(-dy)
		else:
			move_north_n(WORLD_SIZE +dy)



# spawn
def wait_for_all_drones(drones):
	while True:
		total = 0
		for d in drones:
			if has_finished(d):
				total += 1
		if total == len(drones):
			break

def spawn_and_wait_all(fs):
	drones = []
	for f in fs:
		drone = spawn_drone(f)
		if drone != None:
			drones.append(drone)
		else:
			f()
	wait_for_all_drones(drones)

def grid_spawn_and_wait_all(cell_f):
	row_spawn_and_wait_all(to_row_f(cell_f))

def row_spawn(row_f):
	move_to(0,0)
	for _ in range(WORLD_SIZE-1):
		spawn_drone(row_f)
		move(North)
	row_f()
	move(North)

def row_spawn_and_wait_all(row_f):
	move_to(0,0)
	drones = []
	for _ in range(WORLD_SIZE-1):
		drones.append(spawn_drone(row_f))
		move(North)
	row_f()
	move(North)
	wait_for_all_drones(drones)


def column_spawn(column_f):
	move_to(0,0)
	for _ in range(WORLD_SIZE-1):
		spawn_drone(column_f)
		move(East)
	column_f()
	move(East)

def column_spawn_and_wait_all(column_f):
	move_to(0,0)
	drones = []
	for _ in range(WORLD_SIZE-1):
		drones.append(spawn_drone(column_f))
		move(East)
	column_f()
	move(East)
	wait_for_all_drones(drones)

def to_row_f(cell_f):
	def f():
		for _ in range(WORLD_SIZE):
			cell_f()
			move(East)
	return f

def to_column_f(cell_f):
	def f():
		for _ in range(WORLD_SIZE):
			cell_f()
			move(North)
	return f
	
def column_spawn_and_wait_all(column_f):
	move_to(0,0)
	drones = []
	for _ in range(WORLD_SIZE-1):
		drones.append(spawn_drone(column_f))
		move(East)
	column_f()
	move(East)
	wait_for_all_drones(drones)

def spacing_spawn_and_wait_all(cell_f,spacing):
	drones = []
	x = spacing//2
	while x < WORLD_SIZE:
		y = spacing//2
		while y< WORLD_SIZE:
			move_to(x,y)
			drones.append(spawn_drone(cell_f))
			y += spacing
		x += spacing
	wait_for_all_drones(drones)
	
	
# loop

def loop(f, x0, y0, x1, y1):
	for x in range(x0, x1):
		move_to(x,y0)
		for y in range(y0, y1):
			f()
			move(North)


def loop2(f, x0, y0, x1, y1):
	for x in range(x0, x1):
		move_to(x,y0)
		for y in range(y0, y1):
			f(x, y)
			move(North)
def spacing_loop(cell_f,spacing):
	ret = []
	x = spacing //2
	while x < WORLD_SIZE:
		y = spacing //2
		while y < WORLD_SIZE:
			move_to(x,y)
			r = cell_f()
			if r != None:
				ret.append(r)
			y+=spacing			
		x+=spacing
	return ret

# array sort

def sort(arr):
	return quicksort(arr,0,len(arr)-1)

def reverse(arr):
	r = []
	for i in range(len(arr)-1, -1,-1):
		r.append(arr[i])
	return r
	
def quicksort(arr, low, high):
	def partition(arr, low, high):
		pivot = arr[high]  # Choose the last element as the pivot
		i = low - 1        # Pointer for the smaller element boundary
	
		for j in range(low, high):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]  # Swap elements
	
		# Place the pivot in its correct sorted position
		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		return i + 1

	if low < high:
		# Find the partition index where the pivot belongs
		pivot_index = partition(arr, low, high)
		
		# Recursively sort elements before and after partition
		quicksort(arr, low, pivot_index - 1)
		quicksort(arr, pivot_index + 1, high)
	return arr


# dig
	
def dig_until(gt):
	def f():
		while get_ground_type() != gt:
			dig()
	return f

def dig_through(gt):
	def f():
		while get_ground_type() == gt:
			dig()
	return f

def dig_deep_until(gt, z):
	def f():
		while get_pos_z() >= z and get_ground_type() != gt:
			dig()
	return f

def dig_deep(z):
	def f():
		while get_pos_z() >= z:
			dig()
	return f
	
	
	
def dig_all_until(gt):
	f = dig_until(gt)
	row_spawn_and_wait_all(to_row_f(f))

def dig_all_through(gt):
	f = dig_through(gt)
	row_spawn_and_wait_all(to_row_f(f))