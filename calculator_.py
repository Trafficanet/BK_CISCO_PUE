import operator
#inicialmente para realizar la operación directamente entre los números de la consola
dictoper={'1':'+','2':'-','3':'*','4':'/','5':'**'}
#Para lanzar por pantalla la elección de usuario
dictnomoper={'1':'SUMAR','2':'RESTAR','3':'MULTIPLICAR','4':'DIVIDIR','5':'POTENCIAR'}
#Tercer diccionario con llamadas a operator porque fui incapaz de extraer signos sin comillas solo de dictoper
aplicar={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow}
def Numconsola(mensaje):
  while True:
    try:
       numc =float(input(mensaje))
    except ValueError:
       print("No es numero válido! Introdúzcalo en cifras y con un punto de separación de decimales .")
       continue
    else:
       return numc
       break

def Numoper(mensaje):
  while True:
    try:
       numc =int(input(mensaje))
       while numc > 5:
               print('No puedo realizar la operación')
               print("Número Debe ser escoger entre 1 y 5")
               numc= int(input("""Escriba su elección para operar entre ambos números
           		1. para SUMAR ambos números
           		2. para restarlos
           		3. para para MULTIPLICARLOS
           		4. para DIVIDIRLOS
           		5. para potenciar el primero al segundo"""))
    except ValueError:
       print("Número Debe ser menor o igual a 5 .")
       continue
    else:
       return numc
       break

def calq(a,b,c):
        print('Escogió' ,dictnomoper[str(c)],'los números')
        result=aplicar[dictoper[str(c)]](a,b)
        return print("El resultado de la operación es ",str(result))

try:
    numu = Numconsola('Escriba su primer número  : ')
    numd = Numconsola("Escriba su segundo número  : ")
    oped = Numoper("""Escriba su elección para operar entre ambos números
    		1. para SUMAR ambos números
    		2. para restarlos
    		3. para para MULTIPLICARLOS
    		4. para DIVIDIRLOS
    		5. para potenciar el primero al segundo""")
    calq(numu, numd, oped)
except ZeroDivisionError:
    print('No puedo dividir por cero')
    numd = float(input("Por Favor, reintroduzca el denominador : "))
    calq(numu,numd,4)


