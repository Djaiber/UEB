def cesar(msg,n):
    import string

    alpha = string.ascii_uppercase
  
    m =len(msg)
    salida = ""

    for i in range(m):
        c = msg[i]
        loc = alpha.find(c) 
        new_loc = (loc + n) % 26
        salida += alpha[new_loc] 

    return salida
print(cesar("GATO",3))