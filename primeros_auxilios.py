import sys

#1ra respuesta del usuario
resp_1 = input ('¿responde a los estimulos?')

if resp_1 =='si':
    print('valorar la necesidad de llevarlo al hospital mas cercano')
    sys.exit() #finaliza el flujo
else:
    print('Abrir via Aérea')

#2da respuesta del usuario
resp_2 = input ('¿repira?')

if resp_2 =='si':
    print('Permitele posiscion de suficiente ventilación')
    sys.exit()  #finaliza el flujo
else:
    print('Administar 5 ventilaciones y llamar a la ambulancia')

#cliclo while - 3ra respuesta del usuario
ambulancia = 'no'
while ambulancia =='no':

    resp_3 = input ('¿Signos de vida?')

    if resp_3 =='si':
        print('Reevaluar a la espera de la ambulancia')
    else:
        print('Administar compresiones toraxicas hasta que llegue ambulancia')
        
    ambulancia = input('¿llego la ambulancia?')
