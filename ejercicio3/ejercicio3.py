# programa que indique el precio de una venta de un articulo dado.

# input
p_compra = int(input("Ingrese el valor de la compra: "))

# processing
if p_compra<3000:
    ganancia = 500
    p_venta = p_compra + ganancia
else:
    if p_compra>6000:
        ganancia = 500
        p_compra = p_compra + ganancia
    else:
        ganancia = p_compra*0.25
        p_venta = p_compra + ganancia

# ouput
print("El precio de venta es: " + str(p_venta))
