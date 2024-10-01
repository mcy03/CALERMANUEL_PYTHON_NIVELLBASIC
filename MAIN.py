import random
import csv
import os

def adivinaNumero():
    valorR = random.randint(1,10)
    intentos = int(3)

    while intentos > 0:
        numIntento = int(input('En que numero estoy pensando? (1-10) '))

        try:
            if numIntento > 10 or numIntento < 1:
                print('introduce un numero valido porfavor.')
                continue

            if numIntento > valorR:
                print(f'estoy pensando en un numero menor a {numIntento}')
                
            elif numIntento < valorR:
                print(f'estoy pensando en un numero mayor a {numIntento}')
            
            else:
                print(f'Lo has adivinado, el numero es: {numIntento}')
                print('')
                print('-------------------------------------------------------')
                print('----------------------- VICTORY -----------------------')
                print('-------------------------------------------------------')
                print('')
                break;

            intentos -= 1
            print(f'Te quedan {intentos} intentos')

            if intentos < 1:
                
                print('has consumido tus intentos, mas suerte la proxima vez!!')
                print('')
                print('-------------------------------------------------------')
                print('---------------------- GAME OVER ----------------------')
                print('-------------------------------------------------------')
                print('')
                break;
            
        except ValueError:
            print("ingresa un valor valido (1 - 10)")

def piedraPapelTijera():
    opciones = ["piedra", "papel", "tijeras"]

    puntosUser = 0
    puntosEnemigo = 0
   
    while puntosUser < 3 and puntosEnemigo < 3:
        print('------------------------------------------------------')
        print('--------------- Piedra, papel, tijera ----------------')
        print('')
        print('Introduce una opcion:')
        print('- Piedra')
        print('- Papel')
        print('- Tijeras')
        print('')
        valorUser = input('').lower()

        valorEnemigo = random.choice(opciones)

        print(f'El enemigo a elejido {valorEnemigo}')
        result = compararEleccion(valorUser, valorEnemigo)

        print(f'tu: {valorUser} - enemigo: {valorEnemigo}')

        if result == "empate":
            print('habeis empatado')
        elif result == valorUser:
            print('has ganado la ronda!!')
            puntosUser += 1
        else:
            print('has perdido la ronda')
            puntosEnemigo += 1
        
        print('Resumen de puntos:')
        print(f'Tu: {puntosUser}')
        print(f'Enemigo: {puntosEnemigo}')
    
    if puntosUser > 2:
        print('-------------------------------------------------------')
        print('----------------------- VICTORY -----------------------')
        print('-------------------------------------------------------')
    elif puntosEnemigo > 2:
        print('-------------------------------------------------------')
        print('---------------------- GAME OVER ----------------------')
        print('-------------------------------------------------------')

def compararEleccion(valorUser, valorEnemigo):
    if (valorUser == 'piedra' and valorEnemigo == 'tijeras') or (valorUser == 'papel' and valorEnemigo == 'piedra') or (valorUser == 'tijeras' and valorEnemigo == 'papel'):
        return valorUser
    elif valorUser == valorEnemigo: 
        return "empate"
    else:
        return valorEnemigo

def tablero(palabra):
    tablero = ''
    for char in palabra:
        tablero += char # Letra no adivinada
    print(tablero.strip())  # Mostrar el tablero

def ahorcado():
    # Obtener la ruta absoluta del directorio donde está el script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Combinar con el nombre del archivo CSV
    csv_file = os.path.join(current_dir, "palabras.csv")
    
    # Lista para almacenar las palabras
    palabras = []
    letras_descubiertas = []
   
    # Abrir y leer el archivo CSV
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=';')  # Especificar el delimitador ';'
        for row in csv_reader:
            palabras.extend(row)  # Añadir las palabras a la lista

    palabraSeleccionada = random.choice(palabras)
   
    long = len(palabraSeleccionada)
    palabra_a_mostrar = ['_'] * long
    print('------------------------- AHORCADO -------------------------')
    print(f'La palabra a adivinar tiene una longitud de {long} letras, suerte!!')
    intentos = 3

    while intentos > 0:
        tablero(palabra_a_mostrar)
        print(f'Tienes {intentos} intentos para adivinar la palabra')

        letraUser = input('Introduce una letra: ')

        # Verificar si la letra ya fue adivinada
        if letraUser in letras_descubiertas:
            print(f"Ya has usado la letra '{letraUser}'.")
            continue
    
        if letraUser in palabraSeleccionada:
            print(f"Bien hecho, la letra '{letraUser}' se encuentra en la palabra.")
            for i, valor in enumerate(palabraSeleccionada):
                if valor == letraUser:
                    palabra_a_mostrar[i] = letraUser
            


        else:
            print(f"La letra {letraUser} no se encuentra en la palabra.")
            intentos -= 1
    
    if "_" not in palabra_a_mostrar:
        print(f"FELICIDADESS, HAS ACERTADO LA PALABRA")
    else:
        print(f"GAME OVER: otra vez sera...")
    
    print(f"La palabra era {palabraSeleccionada}")

def main():
    while True:
        print('----------------  MENU GAMEROOM ----------------')
        print('-    1: Adivina el numero.')
        print('-    2: Piedra, papel, tijera.')
        print('-    3: Ahorcado.')
        print('-    4: Salir.-')

        opcionUser = int(input("A que jugamos? "))

        try:
            if opcionUser == 1:
                adivinaNumero()
            elif opcionUser == 2:
                piedraPapelTijera()
            elif opcionUser == 3:
                ahorcado()
            elif opcionUser == 4:
                print('Saliendo del menu.')
                break;
        
        except ValueError:
            print("indica un juego valido.")

if __name__ == "__main__":
    main()
