from funcion import tiempo_entrega_entrega_dias

import random
for x in range(10):
    distancia = random.randint(0,2000)
    dias = tiempo_entrega_entrega_dias(distancia)
    print('Para distancia {}km la entraga es en {} dias'.format(distancia, dias))