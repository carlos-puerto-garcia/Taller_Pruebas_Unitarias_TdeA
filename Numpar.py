'''Dice si el numero es par o impar'''
ent=int(input("Ingrese el numero: "))

def numpar(ent):
    if ent == 0:
        txt="El numero debe ser diferente de Cero"
        print (txt)
    elif ent%2 == 0:
        txt="Este numero es par"
        print (txt)
    else:
        txt="Este numero es impar"
        print (txt)
    return txt
