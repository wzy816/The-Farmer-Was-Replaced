# world size

WORLD_SIZE = get_world_size()
HALF_WORLD_SIZE = WORLD_SIZE // 2
WORLD_SIZE_SQ = WORLD_SIZE * WORLD_SIZE

# use item functions


def do_water():
	w = get_water()
	for _ in range(4 - 4 * w):
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


# till functions


def till_to_soil():
	if get_ground_type() != Grounds.Soil:
		till()


# move functions


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


def move_to(x, y, cross_boundary=True):
	dx = x - get_pos_x()
	if dx > 0:
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
	if dy > 0:
		if dy <= HALF_WORLD_SIZE or not cross_boundary:
			move_north_n(dy)
		else:
			move_south_n(WORLD_SIZE - dy)
	else:
		if -dy <= HALF_WORLD_SIZE or not cross_boundary:
			move_south_n(-dy)
		else:
			move_north_n(WORLD_SIZE + dy)


# loop functions
def loop(f, x0, y0, x1, y1):
	for x in range(x0, x1):
		move_to(x, y0)
		for y in range(y0, y1):
			f()
			move(North)


def loop2(f, x0, y0, x1, y1):
	for x in range(x0, x1):
		move_to(x, y0)
		for y in range(y0, y1):
			f(x, y)
			move(North)


# drone functions


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


def row_spawn(row_f):
	move_to(0, 0)
	for _ in range(WORLD_SIZE - 1):
		spawn_drone(row_f)
		move(North)
	row_f()
	move(North)


def row_spawn_and_wait_all(row_f):
	move_to(0, 0)
	drones = []
	for _ in range(WORLD_SIZE - 1):
		drones.append(spawn_drone(row_f))
		move(North)
	row_f()
	move(North)
	wait_for_all_drones(drones)


def column_spawn(column_f):
	move_to(0, 0)
	for _ in range(WORLD_SIZE - 1):
		spawn_drone(column_f)
		move(East)
	column_f()
	move(East)


def column_spawn_and_wait_all(column_f):
	move_to(0, 0)
	drones = []
	for _ in range(WORLD_SIZE - 1):
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


# heapq


def heappush(heap, item):
	heap.append(item)
	_siftdown(heap, 0, len(heap) - 1)


def heappop(heap):
	last = heap.pop()
	if heap:
		return_item = heap[0]
		heap[0] = last
		_siftup(heap, 0)
		return return_item
	return last


def _siftdown(heap, startpos, pos):
	newitem = heap[pos]
	while pos > startpos:
		parentpos = (pos - 1) // 2
		parent = heap[parentpos]
		if newitem < parent:
			heap[pos] = parent
			pos = parentpos
			continue
		break
	heap[pos] = newitem


def _siftup(heap, pos):
	endpos = len(heap)
	startpos = pos
	newitem = heap[pos]
	childpos = 2 * pos + 1
	while childpos < endpos:
		rightpos = childpos + 1
		if rightpos < endpos and heap[childpos] > heap[rightpos]:
			childpos = rightpos
		heap[pos] = heap[childpos]
		pos = childpos
		childpos = 2 * pos + 1
	heap[pos] = newitem
	_siftdown(heap, startpos, pos)


if __name__ == "__main__":
	heap = []
	heappush(heap, (1, "1"))
	heappush(heap, (2, "2"))
	heappush(heap, (2, "3"))
	heappush(heap, (4, "3"))
	heappush(heap, (2, "4"))
	print("Heap:", heap)
	poped = []
	while heap:
		poped.append(heappop(heap))
	print("Poped:", poped)
