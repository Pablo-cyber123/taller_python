while True:
    numero = input("Introduce un número de 4 cifras o más: ")
    if len(numero) >= 4 and numero.isdigit():
        suma = 0
        pares = 0
        impares = 0
        cifras_pares = []
        cifras_impares = []
        for cifra in numero:
            suma += int(cifra)
            if int(cifra) % 2 == 0:
                cifras_pares.append(cifra)
                pares += 1
            else:
                cifras_impares.append(cifra)
                impares += 1
        print(f"Cantidad de cifras del numero: {len(numero)}")        
        print(f"La suma de las cifras es: {suma}")
        print(f"Cifras pares: {', '.join(cifras_pares) if cifras_pares else 'Ninguna'}")
        print(f"Cantidad de cifras pares: {pares}")
        print(f"Cifras impares: {', '.join(cifras_impares) if cifras_impares else 'Ninguna'}")
        print(f"Cantidad de cifras impares: {impares}")
        break
    else:
        print("Por favor, introduce un número válido de al menos 4 cifras.")