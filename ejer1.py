"""
1) Realiza un programa que lea la edad de 3 personas e indique lo siguiente:
* Muestre un mensaje indicando a que grupo pertenece cada persona. _"niño"_, _"adolescente"_ o _"adulto"_ __(un ejemplo para cada grupo)__
* Muestra un error si cualquiera de las edades introducidas es 0
"""

# Para poder clasificar la edad en grupos de niño, adolescente y adulto 
def clasificar_edad(edades):
    grupos = []
    for edad in edades:
        if edad == 0:
            raise ValueError("La edad no puede ser 0")
        elif 1 <= edad <= 12:
            grupos.append("niño")
        elif 13 <= edad <= 18:
            grupos.append("adolescente")
        else:
            grupos.append("adulto")
    return grupos

# Prueba con un ejemplo para cada grupo (asumiendo que el usuario introduce las edades)
edades_de_ejemplo = [10, 16, 30]  # Niño, adolescente y adulto
clasificar_edad(edades_de_ejemplo)



