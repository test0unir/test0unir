def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

resultado = factorial(5)
print("El factorial de 5 es:", resultado)
