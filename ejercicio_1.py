# Funcion que recibe un número n y devuelve una lista.
def par_impar(n):
    resultados = [n]
    # Bucle while que se ejecuta hasta que n sea igual a 1.
    while n != 1: 
        # Verifica si n es par, si es par se divide por 2
        if n % 2 == 0:
            n = n // 2
        else:
            # Si n no es par, se multiplica por 3 y se suma 1
            n = n * 3 + 1
        resultados.append(n)
# Se retorna la lista de resultados
    return resultados

# Caso de prueba
print(par_impar(3))
assert par_impar(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print('Todos los casos de prueba han pasado correctamente.')
