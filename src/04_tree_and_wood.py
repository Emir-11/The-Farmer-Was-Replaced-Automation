# Optimize Edilmiş Kod:
def olgunsatopla():
	if can_harvest():
		harvest()
	if (get_pos_x() + get_pos_y()) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def tarlayi_sur():
	size = get_world_size()
	for x in range(size):
		for y in range(size):

			olgunsatopla()
			move(North)
		move(East)

while True:
	tarlayi_sur()

#Kodun İlk Hali

def olgunsatopla():
	if can_harvest() == True:
		harvest()
	else:
		pass
while True:
	if get_pos_y() % 2 == 0:
		olgunsatopla()
		if get_pos_x() % 2 == 0:
			plant(Entities.Tree)
			move(North)
		else:
			plant(Entities.Bush)
			move(North)
	elif get_pos_y() == 5:
		olgunsatopla()
		if get_pos_x() % 2 == 0:
			plant(Entities.Bush)
			move(North)
			move(East)
		elif get_pos_x() == 5:
			plant(Entities.Tree)
			if get_pos_x() == 5 and get_pos_y() == 5:
				move(North)
				move(East)
			else:
				move(East)
	
		else:
			plant(Entities.Tree)
			move(North)
			move(East)
	else:
		olgunsatopla()
		if get_pos_x() % 2 == 0:
			plant(Entities.Bush)
			move(North)
		else:
			plant(Entities.Tree)
			move(North)