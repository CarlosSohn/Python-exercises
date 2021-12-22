accion = ""
dic = {}
def add():
	nif = int(input("NIF: "))
	name = input("Nombre: ")
	edad = int(input("Edad: "))
	dir = input("Dirección: ")
	tel = int(input("Telefono: "))
	email = input("Email: ")
	pref = input("Cliente preferente? s / n: ")
	if pref in ("S", "s"):
		pref = True
	else:
		pref = False
	data = {'nom' : name, 'edad' : edad, 'dir' : dir, 'tel' : tel, 'email' : email, 'pref' : pref}
	dic[nif] = data
	print("Listo!")
def eliminar(): # Done
	nif = int(input("NIF: "))
	if nif not in dic:
		print("NIF no existente.")
	else:
		dic.pop(nif)
		print("Listo!")
def  show_cli():
	nif = int(input("NIF: "))
	if nif not in dic:
		print("NIF no existente.")
	else:
		alt = dic[nif]
		print("Nom: ", alt['nom'])
		print("Edat: ", alt['edad'])
		print("Adreca: ", alt['dir'])
		print("Telefon: ", alt['tel'])
		print("E-mail: ", alt['email'])
		print("Preferencial?: ", alt['pref'])
def show_tots():
	if dic == {}:
		print("No s'han afegit clients")
	else:
		print("|--- NIF", "---|--- " "Nom ---|")
		for i in dic:
			alt = dic[i]
			print("|---", i, "---|---", alt['nom'], "---|")
def show_prefs():
	if dic == {}:
		print("No s'han afegit clients")
	else:
		print("|--- NIF", "---|--- " "Nom ---|")
		for i in dic:
			alt = dic[i]
			preferencial = alt['pref']
			if preferencial == True:
				print("|---", i, "---|---", alt['nom'], "---|")
			else:
				print("No hi ha preferents")
while accion != 6:
	print("Què vols fer? \n1) Afegir client. \n2) Esborrar client. \n3) Mostrar client. \n4) Llistar tots els clients.")
	print("5) Consultar clients preferents. \n6) Terminar.")
	accion = int(input("Opció número: "))
	if accion == 1:
		add()
	elif accion == 2:
		eliminar()
	elif accion == 3:
		show_cli()
	elif accion == 4:
		show_tots()
	elif accion == 5:
		show_prefs()
	elif accion == 6:
		break
	else:
		break
