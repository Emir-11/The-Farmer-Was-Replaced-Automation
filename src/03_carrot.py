while True:
	if not get_ground_type() == Grounds.Soil:
		till()
		plant(Entities.Carrot)
		move(North)
	
	elif can_harvest() == True:
		harvest()
		plant(Entities.Carrot)
		move(North)
	else:
		move(East)