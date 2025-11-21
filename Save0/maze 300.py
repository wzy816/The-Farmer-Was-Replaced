# 成就：循环利用

clear()
set_world_size(4)

from util import *

dirs = [
	(1, 0, East, West),
	(-1, 0, West, East),
	(0, -1, South, North),
	(0, 1, North, South),
]


def dfs(x, y):
	global visited
	global t_x
	global t_y
	global treasure_cnt
	global total_steps

	# avoid cycle
	if total_steps > WORLD_SIZE_SQ:
		return True

	if get_entity_type() == Entities.Treasure:
		treasure_cnt += 1
		return True

	visited[(x, y)] = 1

	# sort direction candidates by distance to target
	directions = []
	for dx, dy, forward_dir, back_dir in dirs:
		nx, ny = x + dx, y + dy
		if (nx, ny) not in visited and can_move(forward_dir):
			s = abs(nx - t_x) + abs(ny - t_y) + random() * 2
			heappush(directions, (s, nx, ny, forward_dir, back_dir))

	directions_sorted = []
	while directions:
		directions_sorted.append(heappop(directions))

	for s, nx, ny, forward_dir, back_dir in directions_sorted:
		move(forward_dir)
		total_steps += 1
		if dfs(nx, ny):
			return True
		move(back_dir)
		total_steps += 1

	visited.pop((x, y))
	return False


plant(Entities.Bush)
substance = WORLD_SIZE * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)

treasure_cnt = 0
while treasure_cnt < 301:
	if get_entity_type() == Entities.Treasure or treasure_cnt == 0:
		use_item(Items.Weird_Substance, substance)

	visited = {}
	total_steps = 0
	t_x, t_y = measure()
	x, y = get_pos_x(), get_pos_y()
	dfs(x, y)

g = num_items(Items.Gold)
harvest()
print(num_items(Items.Gold) - g)
