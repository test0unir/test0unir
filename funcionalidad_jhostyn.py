def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

frase = input("Ingresa una frase: ")
numero_palabras = contar_palabras(frase)
print("El número de palabras en la frase es:", numero_palabras)