"""
4) Crea una lista de palabras, recorre la lista y muestra cada palabra junto con su longitud. Al final, indicar cual fue la palabra con más caracteres.
"""

# Creamos una lista de palabras
palabras = ["Python", "Desarrollo", "Algoritmo", "Función", "Variable"]

# Inicializamos la palabra más larga y su longitud
palabra_mas_larga = ""
longitud_palabra_mas_larga = 0

# Recorremos la lista y mostramos cada palabra con su longitud
for palabra in palabras:
    longitud = len(palabra)
    print(f"Palabra: {palabra}, Longitud: {longitud}")
    
    # Comprobamos si esta palabra es la más larga hasta ahora
    if longitud > longitud_palabra_mas_larga:
        palabra_mas_larga = palabra
        longitud_palabra_mas_larga = longitud

# Mostramos la palabra con más caracteres
print(f"La palabra con más caracteres es: {palabra_mas_larga}, con {longitud_palabra_mas_larga} caracteres.")
