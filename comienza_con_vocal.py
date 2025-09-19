"""
Integrantes
Carlos Osvaldo Díaz García

Fecha
18 de septiembre de 2025

Determinar si una palabra comienza con una vocal.
"""

# Entradas
palabra = input("Escribe una palabra: ")

# Proceso
letra = palabra[0:1].lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "á" or letra == "é" or letra == "í" or letra == "ó" or letra == "ú":
    # Salida
    print(palabra, "comienza con vocal")
else:
    #Salida
    print(palabra, "no comienza con vocal")