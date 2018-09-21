def positivo(num):
    val = ""
    if(num<0):
        val="Negativo"
    if(num>0):
        val="Positivo"
    if(num==0):
        val = "Neutro"
    return val
