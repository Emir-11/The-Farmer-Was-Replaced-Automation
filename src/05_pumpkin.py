def my_move_to(target_x, target_y):
	while get_pos_x() != target_x:
		if get_pos_x() < target_x:
			move(East)
		else:
			move(West)
	while get_pos_y() != target_y:
		if get_pos_y() < target_y:
			move(North)
		else:
			move(South)

def pumpkin_otomasyon():
	while True:
		tarla_hazir = True
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				my_move_to(x, y)
				if get_entity_type() == None:
					plant(Entities.Pumpkin)
					tarla_hazir = False
				elif get_entity_type() == Entities.Dead_Pumpkin:
					harvest()
					plant(Entities.Pumpkin)
					tarla_hazir = False
				elif can_harvest() < 1:
					tarla_hazir = False
		if tarla_hazir:
			harvest()
			break
while True:
	pumpkin_otomasyon()