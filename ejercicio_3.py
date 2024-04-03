# Dado un número Y y un número X, se determina el valor que se encuentra en la posición (Y, X) de una espiral numérica.
def number_spiral(Y, X):
    # Si Y es mayor que X, se calcula el valor de la espiral en la posición (Y, X) de la espiral numérica.
    if Y > X:
        ans = (Y - 1) * (Y - 1)
        # Si Y es impar, se suma X al valor de la espiral en la posición (Y, Y).
        add = X if Y % 2 != 0 else 2 * Y - X
        return ans + add
    # Si X es mayor que Y, se calcula el valor de la espiral en la posición (Y, X) de la espiral numérica.
    else:
        ans = (X - 1) * (X - 1)
        # Si X es par, se suma Y al valor de la espiral en la posición (X, X).
        add = Y if X % 2 == 0 else 2 * X - Y
        return ans + add    
# Casos de prueba
Y = 2
X = 2
# Se espera que el valor que se encuentra en la posición (Y, X) de la espiral numérica sea 3.
print("El resultado es:", number_spiral(Y, X))
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado exitosamente.")