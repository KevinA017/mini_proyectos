import os
def run():
    os.system("cls")
    cantidad = int(input("Cuantos numeros desea ingresar: "))
    numeros = []
    num_menor = 0
    num_mayor = 0
    for i in range(1, cantidad + 1):
        os.system("cls")
        numero = int(input("Digite un numero: "))
        numeros.append(numero)
        num_menor = numeros[0]
    for i in numeros:
        if i < num_menor:
            num_menor = i
        elif i > num_mayor:
            num_mayor = i
        else:
            continue
    print(f"El numero mayor es: {num_mayor}\nEl numero menor es: {num_menor}")
if __name__ == "__main__":
    run()