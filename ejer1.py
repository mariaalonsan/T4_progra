"""
1) Realiza un programa que lea la edad de 3 personas e indique lo siguiente:
* Muestre un mensaje indicando a que grupo pertenece cada persona. _"niño"_, _"adolescente"_ o _"adulto"_ __(un ejemplo para cada grupo)__
* Muestra un error si cualquiera de las edades introducidas es 0
"""

# Primero definimos una función para determinar el grupo de edad, usamos def para definir una función y return para devolver el valor de la función, el grupo de edad 
def determinar_grupo_de_edad(edad):
    if edad == 0:
        return "Error: La edad no puede ser 0."
    elif edad < 13:
        return "niño"
    elif 13 <= edad < 18:
        return "adolescente"
    else:
        return "adulto"

# Hacemos el ejemplo de las edades
edades = [5, 0, 20]  

# Para determinar el grupo de edad de cada persona, usamos un bucle for, que recorre la lista de edades, y para cada edad, determina el grupo de edad usando la función que definimos antes
# Vamos a usar enumerate para obtener el índice de cada edad, empezando en 1
for i, edad in enumerate(edades, 1):
    grupo = determinar_grupo_de_edad(edad)
    if "Error" in grupo:
        print(grupo)
    else:
        print(f"La persona {i} de {edad} años es un {grupo}.")




