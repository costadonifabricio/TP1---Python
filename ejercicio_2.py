# Funcion para encontrar el número faltante en la lista.
def encontrar_numero(n, numeros):
    return (n * (n + 1)) // 2 - sum(numeros)

# Casos de prueba
resultado = encontrar_numero(5, [1, 2, 4, 5])
assert encontrar_numero(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
print("El numero faltante es:", resultado)
print('Todos los casos de prueba han pasado correctamente.')
