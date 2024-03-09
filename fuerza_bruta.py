from string import ascii_lowercase
from getpass import getpass

# solicita al ususario ingresar contrseña ocullta
contraseña = getpass("Ingrese la contraseña: ")


#ciclo for anidado
intentos = 0

for caracter in contraseña: #itera sobre la contraseña
    for letra in ascii_lowercase:#itera sobre el abededario
        intentos += 1 #cuenta numero de intentos 
        if caracter == letra: #compara el caracter de la contrasena con la letra de abecesario
            break

print(f"La contraseña fue forzada en {intentos} intentos")
