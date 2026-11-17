
from util import *


def dig_coal():
	dig_all_until(Grounds.Dirt)
	
	STEP=HALF_WORLD_SIZE//2
	SPACING=HALF_WORLD_SIZE
	
	z = get_pos_z()
	
	while True:
		
		# spacing drill one STEP deep
		def d0(target_z):
			def f():
				while get_pos_z() >= target_z and get_ground_type() == Grounds.Dirt:
						dig()
			return f
		spacing_spawn_and_wait_all(d0(z-STEP), SPACING)
		

		# probe
		def p():
			return (get_pos_z(), get_ground_type())

		coal_depths = []
		reaching_non_dirt = False
		for d in spacing_loop(p, SPACING):
			if d[1] == Grounds.Coal:
				coal_depths.append(d[0])
			elif d[1] != Grounds.Dirt:
				reaching_non_dirt = True
				
		# exit when reaching non-dirt
		if reaching_non_dirt:
			break
		
		# mine coal layers
		if len(coal_depths)>0:
			for d in reverse(sort(list(set(coal_depths)))):
				grid_spawn_and_wait_all(dig_deep(d))
				
		# drill everything within STEP
		grid_spawn_and_wait_all(dig_deep(z-STEP))
		
		z = z-STEP	
		
	dig_all_through(Grounds.Dirt)
	
	
# clear()
dig_coal()

	
	
	
	
	
	
	
	
	
	
