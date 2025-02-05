def pseudoaloatorio(semilla, cantidad):
    multiplicador = 5
    cons_aditiva = 7
    modulo = 8
    pseudoaloatorios = []
    x = semilla

    for _ in range(cantidad):
        semilla = (multiplicador * x + cons_aditiva) % modulo
        pseudoaloatorios.append(x/modulo)
        
        return pseudoaloatorios
L = pseudoaloatorio(3, 10)
print(L)

