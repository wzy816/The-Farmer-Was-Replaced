from util import *

# 南瓜 demo


def main():

	def f1(x, y):
		till_to_soil()
		plant(Entities.Pumpkin)
		not_harvested.append((x, y))

	clear()

	while True:
		not_harvested = []
		loop2(f1, 0, 0, WORLD_SIZE, WORLD_SIZE)

		while True:
			l = []
			for x, y in not_harvested:
				move_to(x, y)
				if can_harvest():
					do_water()
					continue
				else:
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
					l.append((x, y))

			not_harvested = l
			if len(not_harvested) == 0:
				break
		do_harvest_water()


if __name__ == "__main__":
	while True:
		main()
