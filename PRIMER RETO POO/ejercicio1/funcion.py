def mi_propia_funcion(texto=''):
    index = len(texto)
    output = ''
    for idx in range(index):
        output += texto[index - 1 - idx]

    return output
