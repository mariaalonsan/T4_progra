"""
2) Realiza un programa que pida al usuario que ingrese el precio de un producto y luego le pregunte si desea calcular el precio con o sin IVA (un valor numérico para 21% de IVA).
* Calcula el precio final 
* Muestra el resultado.
"""

# Definimos una función para calcular el precio con IVA
def calcular_precio_con_iva(precio):
    IVA = 0.21
    return precio * (1 + IVA)

# Definimos otra función para calcular el precio sin IVA
def calcular_precio_sin_iva(precio):
    return precio

# Vamos a pedir al usuario que ingrese el precio del producto
precio_producto = int(input("Ingrese el precio del producto: "))

# Vamos a preguntar también al usuario si desea calcular el precio con o sin IVA
opcion_iva = input("Desea calcular el precio con IVA? (si/no): ")

# Y por último vamos a calcular y mostrar el resultado
if opcion_iva.lower() == 'si':
    precio_final = calcular_precio_con_iva(precio_producto)
    print(f"El precio final con IVA es: {precio_final:.2f}")
else:
    precio_final = calcular_precio_sin_iva(precio_producto)
    print(f"El precio final sin IVA es: {precio_final:.2f}")
