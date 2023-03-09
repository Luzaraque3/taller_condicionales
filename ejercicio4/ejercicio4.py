# programa que calcule el índice de masa corporal de una persona

# input

p =int(input("ingrese el peso(kg): "))
a =float(input("ingrese la altura(m): "))

# processing

IMC = p/(a*a)

if IMC<16:
    DIAGNOSTICO=("Criterio de ingreso en hospital")
else:
    if 16<= IMC <=17 :
        DIAGNOSTICO=("Infrapeso")
    else:
        if 17<= IMC <=18:
            DIAGNOSTICO=("Bajo peso")
        else:
            if 18<= IMC <=25:
                DIAGNOSTICO=("peso normas(saludable)")
            else:
                if 25<= IMC <=30:
                    DIAGNOSTICO=("Sobrepeso (obesidad de grado I)")
                else:
                    if 30<= IMC <=35:
                        DIAGNOSTICO=("Sobrepeso cronico (obesidad de grado II)")
                    else:
                        if 35<= IMC <=40:
                            DIAGNOSTICO=("Sobrepeso cronico (obesidad de grado III)")
                        else:
                            IMC>40
                            DIAGNOSTICO=("Sobrepeso cronico (obesidad de grado IV)")
            
            
# output

print("el diagnostico es: " + (DIAGNOSTICO))