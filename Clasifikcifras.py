a=float(input("Escriba un número a continuación"))

if a<20.0:
	print(" el número que imprimió es PEQUEÑITO "," en concreto introdujo: ", str(a))
elif a>=20.0 and a<40.0:
	print(" el número que imprimió es MEDIANO "," en concreto introdujo: ", str(a))
elif a>=40.0 and a<60.0:
	print(" el número que imprimió es GRANDE "," en concreto introdujo: ", str(a))
else:
	print(" el número que imprimió es GIGANTE "," en concreto introdujo: ", str(a))