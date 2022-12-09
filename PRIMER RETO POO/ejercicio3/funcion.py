#Para calcular el tiempo de entrada por sobre los 500 se utilizo una funcion recursiva

def tiempo_entrega_entrega_dias(distancia):
    dias = 0
    if distancia < 100:
        dias = 0
    elif distancia < 200:
        dias = 1
    elif distancia < 300:
        dias = 1
    elif distancia < 400:
        dias = 2
    elif distancia < 500:
        dias = 3
    else:
        n1 = tiempo_entrega_entrega_dias(distancia - 100)
        n2 = tiempo_entrega_entrega_dias(distancia - 200)
        dias = n1 + n2

    return dias
