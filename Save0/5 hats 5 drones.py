from util import *

# 成就：时装秀

hats = [
	Hats.Brown_Hat,
	Hats.Cactus_Hat,
	Hats.Carrot_Hat,
	Hats.Gold_Hat,
	Hats.Gray_Hat,
	Hats.Green_Hat,
	Hats.Pumpkin_Hat,
	Hats.Purple_Hat,
	Hats.Straw_Hat,
	Hats.Sunflower_Hat,
	Hats.Tree_Hat,
	Hats.Wizard_Hat,
]


def wear():
	x = random() * WORLD_SIZE // 1
	y = random() * WORLD_SIZE // 1
	move_to(x, y)

	i = random() * len(hats) // 1
	change_hat(hats[i])
	for _ in range(4000):
		do_a_flip()


clear()
for _ in range(max_drones()):
	spawn_drone(wear)
