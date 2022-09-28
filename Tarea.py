# punto 1 IF

numeroIF = 2

if numeroIF < 0:
    print("El numero es Negativo")

elif numeroIF > 0:
    print("El numero es positivo")

else:
    print("el numero es 0")


# punto 2 while

numeroWhile = 2
contador = 0
while contador <= 10:
    numeroWhile = numeroWhile +1
    contador = contador +1
    print(f"El numero es " + str(numeroWhile))

# Do While, Python no tiene do while la condicion seria que se ejecute al menos una vez. 

numeroWhile = 2
contador = 0

while contador <= 10:
    if numeroWhile < 3:
        print("El numero es " + str(numeroWhile))
        break
    else:
        numeroWhile = numeroWhile +1
        contador = contador +1
        print(f"El numero es " + str(numeroWhile))

# Bucle for 

numeroFor = 0

for i in range(0, 3):
    numeroFor = numeroFor +1
    print(numeroFor)


# Switch No existe en Python pero se puede simular

estacion = input("Escribe la estacion del Año: ")

if estacion == "verano":
    print("Estamos en Verano")

elif estacion == "Invierno":
    print("Estamos en Invierno")

elif estacion == "primavera":
    print("Estamos en Primavera")

elif estacion == "otoño":
    print("Estamos en Otoño")

else: 
    print(f"{estacion} no es una estacion del año")
