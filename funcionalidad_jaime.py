def es_palindromo(palabra):
    return palabra == palabra[::-1]

texto = "anita lava la tina"
if es_palindromo(texto.replace(" ", "").lower()):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
