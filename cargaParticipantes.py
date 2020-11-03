from distanciaAlOrigen import distanciaAlOrigen
from promedio import promedioDisparos
from mejorDisparo import mejorDisparo

def cargaParticipantes():

    auxDisparoX = 0
    auxDisparoY = 0
    listaParticipantes = []
    auxListaId = []

    while True:

        datosParticipante = {
            'numeroId': 0,
            'nombreApellido': '',
            'edad': 0,
            'sexo': '',
            'ubicacionDisparo (1,2,3)': [],
            'mejorDisparo': 0,
            'promedioDisparo': 0
        }
        datosParticipante['numeroId'] = int(input("Ingrese el número del participante (999 para finalizar): "))

        auxListaId.append(datosParticipante['numeroId'])
        while auxListaId.count(datosParticipante['numeroId']) > 1:    
            print("Número de participante ya seleccionado, ingrese otro número de identificación")
            datosParticipante['numeroId'] = int(input("Ingrese el número del participante (999 para finalizar): "))
            auxListaId.append(datosParticipante['numeroId'])

        #Salida del programa{
        if datosParticipante['numeroId'] == 999:
            if len(listaParticipantes) == 0:
                print("No se cargó ningún participante.")
            print("Finalizó la carga de participantes.")
            break
        #}

        else:
            datosParticipante['nombreApellido'] = input("Ingrese el nombre y apellido del participante: ").lower()
            datosParticipante['edad'] = int(input("Ingrese la edad del participante: "))
            datosParticipante['sexo'] = input("Ingrese el sexo del participante (F/M): ").upper()

            for disparo in range(3):
                auxDisparoX = float(input(f"Ingrese la coordenada del disparo {disparo+1} en X: "))
                while auxDisparoX < -80 or auxDisparoX > 80:
                    print("Número fuera de rango, ingrese un número entre (-80; 80)")
                    auxDisparoX = float(input(f"Ingrese la coordenada del disparo {disparo+1} en X: "))

                auxDisparoY = float(input(f"Ingrese la coordenada del disparo {disparo+1} en Y: "))
                while auxDisparoY < -80 or auxDisparoY > 80:
                    print("Número fuera de rango, ingrese un número entre (-80; 80)")
                    auxDisparoY = float(input(f"Ingrese la coordenada del disparo {disparo+1} en Y: "))
                
                datosParticipante['ubicacionDisparo (1,2,3)'].append(distanciaAlOrigen(auxDisparoX, auxDisparoY))

        datosParticipante['mejorDisparo'] = mejorDisparo(datosParticipante['ubicacionDisparo (1,2,3)'])
        datosParticipante['promedioDisparo'] = promedioDisparos(datosParticipante['ubicacionDisparo (1,2,3)'])

        listaParticipantes.append(datosParticipante)

    return listaParticipantes