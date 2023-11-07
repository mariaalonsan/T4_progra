"""
2) Realiza un programa que pida al usuario que ingrese el precio de un producto y luego le pregunte si desea calcular el precio con o sin IVA (un valor numérico para 21% de IVA).
* Calcula el precio final 
* Muestra el resultado.
"""

# Función para calcular el precio final de un producto con o sin IVA
def calcular_precio_final(precio, incluir_iva):
    iva = 0.21  # 21% de IVA
    precio_final = precio * (1 + iva) if incluir_iva else precio
    return precio_final

# Simulación de la entrada del usuario
precio_producto = 100  # Precio del producto introducido por el usuario
incluir_iva = True  # El usuario elige calcular el precio con IVA

# Llamada a la función y muestra del resultado
precio_final = calcular_precio_final(precio_producto, incluir_iva)

