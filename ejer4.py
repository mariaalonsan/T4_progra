"""
4) Crea una lista de palabras, recorre la lista y muestra cada palabra junto con su longitud. Al final, indicar cual fue la palabra con más caracteres.
"""

# Creamos la lista de palabras
lista = ["python", "gato", "programación", "función", "perro"]

# Definimos una variable para guardar la palabra con más caracteres y otra para guardar la longitud de esa palabra
palabra_mas_larga = ""
longitud_palabra_mas_larga = 0

# Vamos a recorrer la lista de palabras
for palabra in lista:
    longitud = len(palabra)
    print(f"Palabra: {palabra}, Longitud: {longitud}")
    
    # Si la longitud de la palabra actual es mayor que la longitud de la palabra con más caracteres, actualizamos la palabra con más caracteres y su longitud
    if longitud > longitud_palabra_mas_larga:
        palabra_mas_larga = palabra
        longitud_palabra_mas_larga = longitud

print(f"La palabra con más caracteres es: {palabra_mas_larga}, con {longitud_palabra_mas_larga} caracteres.")
