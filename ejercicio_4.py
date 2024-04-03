# Dada una cadena de caracteres, se debe reorganizar los caracteres de la cadena de tal forma que se forme un palíndromo.
def reorganizar_palindromo(s):
    # Se convierte la cadena a minúsculas
    s = s.lower()
    # Se crea un diccionario para almacenar la frecuencia de cada caracter
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    # Se crea una cadena para almacenar la mitad del palíndromo
    mitad_palindromo = ""
    char_impar = ""
    for char, count in freq.items():
        if count % 2 == 0:
            mitad_palindromo += char * (count // 2)
        else:
            if char_impar:
                return "NO SOLUTION"
            char_impar = char
    # Se crea el palíndromo
    palindromo = mitad_palindromo + char_impar + ''.join(reversed(mitad_palindromo))
    return palindromo
# Se solicita ingresar una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")
resultado = reorganizar_palindromo(cadena)
print("El resultado es:", resultado)
# Casos de prueba
assert reorganizar_palindromo("aabbc") == "abcba", "Error en el caso de prueba"
print("Todos los casos de prueba han pasado exitosamente.")
