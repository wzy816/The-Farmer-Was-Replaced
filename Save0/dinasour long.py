from util import *

# 成就：长龙

clear()
while True:
	change_hat(Hats.Dinosaur_Hat)

	while True:
		move_north_n(WORLD_SIZE - 1)
		for _ in range(HALF_WORLD_SIZE - 1):
			move(East)
			move_south_n(WORLD_SIZE - 2)
			move(East)
			move_north_n(WORLD_SIZE - 2)
		move(East)
		move_south_n(WORLD_SIZE - 1)
		move_west_n(WORLD_SIZE - 1)
		if not move(North):
			break

	change_hat(Hats.Gray_Hat)
