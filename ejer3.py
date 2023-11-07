"""
3) Realiza un programa que lea letras y cuente con una variable contador las letras "a" que se introducen. Para salir del programa, introducir el carácter ".". Al finalizar mostrar el número de veces que se ha pulsado la letra "a".
"""

# Primero definimos una variable contador para las letras "a"
contador_a = 0

# Luego definimos una lista de letras que el usuario va a introducir
letras_introducidas = ['a', 'b', 'a', '.', 'c', 'a']

# Vamos a recorrer la lista de letras introducidas, y para cada letra, incrementamos el contador si la letra es "a"
for letra in letras_introducidas:
    if letra == '.':
        break
    if letra == 'a':
        contador_a += 1

# Por último, printeamos el número de veces que se pulsó la letra "a"
print(f"El número de veces que se pulsó la letra 'a' es: {contador_a}")