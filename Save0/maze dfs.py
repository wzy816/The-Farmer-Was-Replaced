from util import *

# 迷宫 demo
clear()

directions = [
	(1, 0, East, West),
	(-1, 0, West, East),
	(0, -1, South, North),
	(0, 1, North, South),
]


def find_treasure(treasure_x, treasure_y):
	start_x, start_y = get_pos_x(), get_pos_y()
	visited = {}

	def dfs(x, y):
		if x == treasure_x and y == treasure_y:
			return True

		visited[(x, y)] = 1

		for dx, dy, direction, back_direction in directions:
			nx, ny = x + dx, y + dy
			if (nx, ny) not in visited and can_move(direction):
				move(direction)
				if dfs(nx, ny):
					return True
				move(back_direction)

		visited.pop((x, y))
		return False

	# guaranteed to find the treasure
	dfs(start_x, start_y)


while True:
	move_to(0, 0)

	# init maze
	plant(Entities.Bush)
	substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

	treasure_x, treasure_y = measure()
	print("Treasure", treasure_x, treasure_y)

	find_treasure(treasure_x, treasure_y)
	harvest()
