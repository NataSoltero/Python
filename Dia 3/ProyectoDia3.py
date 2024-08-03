texto = input("Ingresa un texto a eleccion: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercer letra: ").lower())

print("\n")
print("Cantidad de letras")
cantidadL = texto.count(letras[0])
cantidadL1 = texto.count(letras[1])
cantidadL2 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidadL} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidadL1} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidadL2} veces")

print("\n")
print("Cantidad de palabras")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("Letras de inicio y fin")

inicio = texto[0]
fin = texto[-1]

print(f"La letra inicial es '{inicio}' y la final es '{fin}'")

print("\n")
print("Texto invertido")

palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos el texto al revees va a decir '{texto_invertido}'")

print("\n")
print("Buscando la palabra Python")

buscar = 'python' in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'Python' {dic[buscar]} se encuentra en el texto")
