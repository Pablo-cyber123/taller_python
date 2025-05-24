
while True:
    numero = input("Introduce un número de 4 cifras o más: ")
    if len(numero) >= 4 and numero.isdigit():
        suma = sum(int(cifra) for cifra in numero)
        print(f"La suma de las cifras es: {suma}")

        pares = [cifra for cifra in numero if int(cifra) % 2 == 0]
        impares = [cifra for cifra in numero if int(cifra) % 2 != 0]

        print(f"Cifras pares: {', '.join(pares) if pares else 'Ninguna'}")
        print(f"Cantidad de cifras pares: {len(pares)}")
        print(f"Cifras impares: {', '.join(impares) if impares else 'Ninguna'}")
        print(f"Cantidad de cifras impares: {len(impares)}")
        break
    else:
        print("Por favor, introduce un número válido de al menos 4 cifras.")

