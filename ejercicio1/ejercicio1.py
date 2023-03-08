# Programa para leer cordenadas en el plano cartesiano y para saber el cuadrante


print("------------------------------------------------------")
print("Programa para indicar el cuadrante de unas coordenadas")
print("------------------------------------------------------")

# input

x = float(input("Digite la coordenada x: "))
y = float(input("Digite la coordenada y: "))

# processing

if x == 0:
    if y == 0:
        msj = ("Las coordenadas corresponden al origen")
    else:
        msj = ("Las coordenadas corresponden al eje y")
else:
    if y == 0:
        msj = ("Las coordenadas corresponden al eje x")
    else:
        if x > 0:
            if y > 0:
                msj = ("Las coordenadas corresponde al cuadrante 1")
            else:
                msj = ("Las coordenadas corresponde al cuadrante 4")
        else:
            if y < 0:
                msj = ("Las coordenadas corresponde al cudrante 3")
            else:
                msj = ("Las coordenadas corresponde al cuadrante 2")
# output

print("-------------------------------------------------------")
print("estas son las coordenadas y cuadrantes de los ejes x,y ")
print("-------------------------------------------------------")
print()
print()

print(msj)