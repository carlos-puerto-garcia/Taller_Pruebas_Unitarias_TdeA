"calcular el factorial"

def Factorial(factorial):
    result = 1
    for i in range(factorial+1):
        if i==0:
            i=1
            result=i * result
        else:
            result=i * result
            print(i," :",result)
    return result


