def es_palindromo(palabra):
    return palabra == palabra[::-1]

texto = "Cambio de frase para commit practica unir"
if es_palindromo(texto.replace(" ", "").lower()):
    print("Cambios propuestos.")
else:
    print("Modificacion Texto.")
