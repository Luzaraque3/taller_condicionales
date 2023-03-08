# Programa que erimita realizar un prestamo

print("-------------------------------------------")
print("Programa para realizar un prestamo bancario")
print("-------------------------------------------")

# input
ing=int(input("Digite sus ingresos mansuales: "))
deu=int(input("Digite su numero de deudas: "))

# processing 
if ing>945000:
    if deu==0:
        rta=("Prestamo aprobado")
    else:
        rta=("Prestamo no aprobado")
else:
    rta=("Prestamo no aprobado")

# ouput 
print("")
print("-----------------------------")
print("---Resultados del prestamo---")
print("-----------------------------")
print("")
print(rta)