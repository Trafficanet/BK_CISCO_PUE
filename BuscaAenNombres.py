listorningan=["Manuelita","Pepe","Ivan","Abundio", "Maño", "Esteban", "Pedro", "Alba","Úrsula","Tere",'Orson',"Begoña"]
selected=[]
for element in listorningan:
	print("Analizando", element, ".......")
	if "a" in element.lower():
		selected.append(element)


print(" Hubo " ,len(selected), " coincidiencias los nombres fueron", selected)
print ("Fin de la lista de resultados coincidentes")
