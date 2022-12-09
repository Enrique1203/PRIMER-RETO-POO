# todo Explicacion de las Funciones
# todo Se crearon dos funciones
# todo num_div: determina el numero de divisores para numero ingresado retornando la cantidad encontrada
# todo create_fibonacci_list: creador de serie de fibonacci desde 0 al numero limite entregado como
# todo parametro de entrada para la busqueda de divisores

def create_fibonacci_list(limit=1):
        prev = 0
        curr = 1
        count = 0
        while True:
            aux = curr
            curr += prev
            prev = aux
            resultado = num_div(curr)
            count += 1
            if count % 10 == 0:
                print('Revisando numero {} - posicion {} ....'.format(curr, count))
            if resultado > limit:
                print('Encontrado numero {} tiene {} divisores'.format(curr, resultado))
                break
        print("Fin del proceso")


def num_div(num=0):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count
