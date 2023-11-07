"""
3) Realiza un programa que lea letras y cuente con una variable contador las letras "a" que se introducen. Para salir del programa, introducir el carácter ".". Al finalizar mostrar el número de veces que se ha pulsado la letra "a".
"""

# Definimos una variable contador para las letras "a"
contador_a = 0

# Simulamos la entrada de letras por el usuario
# Esta es una lista de letras que simulan la entrada del usuario
letras_introducidas = ['a', 'b', 'a', '.', 'c', 'a']

# Procesamos cada letra como si el usuario la hubiera introducido
for letra in letras_introducidas:
    if letra == '.':
        break
    if letra == 'a':
        contador_a += 1

# contador_a contiene el número de veces que se pulsó la letra "a"
