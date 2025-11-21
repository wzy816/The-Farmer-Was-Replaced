from util import *

# 恐龙 demo


def astar(blocked, start, target):
	def heuristic(a, b):
		r = 0
		if a[0] > b[0]:
			r += (a[0] - b[0]) * 1.1
		else:
			r += (b[0] - a[0]) * 0.9
		if a[1] > b[1]:
			r += (a[1] - b[1]) * 1.0
		else:
			r += (b[1] - a[1]) * 0.8
		return r

	if start == target:
		return None, None
	if (
		target[0] < 0
		or target[1] < 0
		or target[0] > WORLD_SIZE - 1
		or target[1] > WORLD_SIZE - 1
	):
		return None, None

	open_set = [(0, 0, start[0], start[1])]

	came_from = {start: None}
	g_score = {start: 0}

	while open_set:
		cur_f, cur_g, cur_x, cur_y = heappop(open_set)

		cur_pos = (cur_x, cur_y)
		if cur_pos == target:
			path = []
			while cur_pos != None:
				path.append(cur_pos)
				cur_pos = came_from[cur_pos]
			return path[::-1], None

		for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			nx = cur_x + dx
			ny = cur_y + dy
			next_pos = (nx, ny)

			if (
				(0 <= nx <= WORLD_SIZE - 1)
				and (0 <= ny <= WORLD_SIZE - 1)
				and next_pos not in blocked
			):
				next_g = cur_g + 1
				if next_pos not in g_score or next_g < g_score[next_pos]:
					g_score[next_pos] = next_g
					next_f = next_g + heuristic(next_pos, target)
					heappush(open_set, (next_f, next_g, nx, ny))
					came_from[next_pos] = cur_pos

	# find path to max g_score pos
	max_g_score = 0
	cur_pos = None
	for k in g_score:
		v = g_score[k]
		if v > max_g_score:
			max_g_score = v
			cur_pos = k
	if cur_pos == None:
		return None, None

	path_to_max_g_score_pos = []
	while cur_pos != None:
		path_to_max_g_score_pos.append(cur_pos)
		cur_pos = came_from[cur_pos]
	return None, path_to_max_g_score_pos[::-1]


while True:
	clear()

	move_to(0, 0)
	change_hat(Hats.Dinosaur_Hat)
	last_apple_x, last_apple_y = 0, 0
	apple_x, apple_y = measure()

	snake = []
	snake_size = 1

	while True:
		cur_x, cur_y = get_pos_x(), get_pos_y()

		# find path to apple, to snake tail, or to furtherst
		path_to_apple, path_with_max_g_score = astar(
			snake, (cur_x, cur_y), (apple_x, apple_y)
		)

		if path_to_apple != None:
			path = path_to_apple
		else:
			path_to_tail, _ = astar(
				snake[1:], (cur_x, cur_y), (snake[0][0], snake[0][1])
			)

			if path_to_tail != None:
				path = path_to_tail
			elif path_with_max_g_score != None:
				path = path_with_max_g_score
			else:
				move_around = False

				for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
					p_x = cur_x + dx
					p_y = cur_y + dy
					p_path, _ = astar(snake, (cur_x, cur_y), (p_x, p_y))
					if p_path != None:
						path = p_path
						move_around = True
						break

				if not move_around:
					quick_print(snake_size)
					break

		# add tail+1
		if cur_x == last_apple_x and cur_y == last_apple_y:
			snake_size += 1

		# move along path, path=[start,...,target]
		for pos in path[1:]:
			move_to(pos[0], pos[1], False)
		snake = snake + path[1:]
		snake = snake[-snake_size:]

		# get new apple
		if get_pos_x() == apple_x and get_pos_y() == apple_y:
			last_apple_x, last_apple_y = apple_x, apple_y
			apple_x, apple_y = measure()

	change_hat(Hats.Gray_Hat)
