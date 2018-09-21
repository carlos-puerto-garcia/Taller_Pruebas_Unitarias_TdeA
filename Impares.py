def Impares(numero):
    numero = str(numero)
    impar = 0
    for elemento in numero :
        elemento = int(elemento)
        if elemento % 2 != 0:
            impar = impar + 1
    return impar



