# name = input("Cual es tu nombre?")
# 	for i in name:
# 		if "Tobari" in name:
# 			print("Te amoooo :D")
# 		else:
# 			print("wakala")

# while True:
# 	name = input("cual es tu nombre?")

# 	if name != "Tobari":
# 		print("wakala")
# 	else:
# 		print("te quero")
# 		break

# name = input("cual es tu nombre?")
# while name != "Tobari":
# 	name = input("cual es tu nombre?")
# 	if name == "Tobari":
# 		print("Te querooo :D")
# 		break
# 	else:
# 		print("wakala")

nombre_correcto = False
while not nombre_correcto:
	name = input("cual es tu nombre?")
	if name == "Tobari":
		print("Te quierooo")
		nombre_correcto = True
	else:
		print("wakala")
	