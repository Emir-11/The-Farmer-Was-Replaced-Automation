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

def dinamik_ekim_otomasyonu():
	res = get_companion()
	
	if res == None:
		if get_entity_type() == None:
			plant(Entities.Bush)
		else:
			move(East)
		return 

	bitki_tipi = res[0]
	koordinat_paketi = res[1]
	hedef_x = koordinat_paketi[0]
	hedef_y = koordinat_paketi[1]
	
	my_move_to(hedef_x, hedef_y)
	
	if get_water() < 0.6:
		use_item(Items.Water)
		
	if can_harvest():
		harvest()
		
	if get_entity_type() != bitki_tipi:
		plant(bitki_tipi)

while True:
	dinamik_ekim_otomasyonu()