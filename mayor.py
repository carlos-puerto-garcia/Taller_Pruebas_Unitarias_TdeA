
#A=int(input("ingrese un para comparar si es mayor numero\n"))
#B=int(input("ingrese otro numero para comparar si es mayor\n"))
#C=int(input("ingrese un nuemero para comparar si es mayor\n"))
def mayor(A,B,C):
    var = 0
    if(A > B and A > C):
        print("El numero mayor es " + str(A))
        var = A
    else:
        if(B > A and B > C):
            print("El numero mayor es " + str(B))
            var = B
        else:
            print("El numero mayor es " + str(C))
            var = C
    return var
