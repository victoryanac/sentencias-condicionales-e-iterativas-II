import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}


#valor ingresado por el usuario
umbral = int(sys.argv[1])

#Comprehensions for de diccionario con filtro de busqueda if
ventas_umbral = {mes : valor for mes, valor in ventas.items() if valor >= umbral}

print(ventas_umbral)
