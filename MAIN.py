# Importamos librerías necesarias para el juego.
import random
import csv
import os

def adivinaNumero():
    # Obtenemos un valor aleatorio entre 1 y 10.
    valorR = random.randint(1,10)

    intentos = int(3)
    
    while intentos > 0: 
        # le pedimos al jugador que intente adivinar el numero en un cierto rango (1-10)
        numIntento = int(input('En que numero estoy pensando? (1-10) '))
        
        try:
            # si el numero introducido es mayor a 10 o menor a 1, nos indicara que el numero introducido no es valido.
            if numIntento > 10 or numIntento < 1:
                print('introduce un numero valido porfavor.')
                continue

            # si el numero introducido es mayor que el aleatorio, nos indicara que el numero introducido es menor que el aleatorio.
            if numIntento > valorR:
                print(f'estoy pensando en un numero menor a {numIntento}')
            
            # si el numero introducido es menor que el aleatorio, nos indicara que el numero introducido es mayor que el aleatorio.
            elif numIntento < valorR:
                print(f'estoy pensando en un numero mayor a {numIntento}')

            # si el numero introducido es igual al aleatorio, nos indicara que el jugador a ganado la partida.
            else:
                # si el jugador ha adivinado el numero, se muestra un mensaje de victoria
                print(f'Lo has adivinado, el numero es: {numIntento}')
                print('')
                print('-------------------------------------------------------')
                print('----------------------- VICTORY -----------------------')
                print('-------------------------------------------------------')
                print('')
                break;

            # si el jugador no ha adivinado el numero, se muestra un mensaje de los intentos restantes
            intentos -= 1
            print(f'Te quedan {intentos} intentos')

            if intentos < 1:
                # si el jugador se a quedado sin intentos, se muestra un mensaje de derrorta
                print('has consumido tus intentos, mas suerte la proxima vez!!')
                print('')
                print('-------------------------------------------------------')
                print('---------------------- GAME OVER ----------------------')
                print('-------------------------------------------------------')
                print('')
                break;
        # si el jugador no ha introducido un valor valido, se muestra un mensaje de error
        except ValueError:
            print("ingresa un valor valido (1 - 10)")

def piedraPapelTijera():
    # opciones de de eleccion  de la maquina
    opciones = ["piedra", "papel", "tijeras"]

    # puntos de la maquina y el usuario
    puntosUser = 0
    puntosEnemigo = 0
    
    # entramos en bucle mientras ningun jugador haya ganado 3 veces
    while puntosUser < 3 and puntosEnemigo < 3:
        # mostramos el menu de opciones para el usuario
        print('------------------------------------------------------')
        print('--------------- Piedra, papel, tijera ----------------')
        print('')
        print('Introduce una opcion:')
        print('- Piedra')
        print('- Papel')
        print('- Tijeras')
        print('')
        valorUser = input('').lower()

        # elegimos un valor aleatorio entre las opciones
        valorEnemigo = random.choice(opciones)

        # mostramos el valor elegido por la maquina
        print(f'El enemigo a elejido {valorEnemigo}')

        # comparamos los valores elegidos por el usuario y la maquina
        result = compararEleccion(valorUser, valorEnemigo)

        # se muestra un resumen de las opciones seleccionadas por cada jugador
        print(f'tu: {valorUser} - enemigo: {valorEnemigo}')
        
        # si el resultado es "empate", se muestra un mensaje de empatado
        if result == "empate":
            print('habeis empatado')
        # si el resultado es el valor elegido por el usuario, se muestra un mensaje de ronda ganada y se suma un punto al usuario
        elif result == valorUser:
            print('has ganado la ronda!!')
            puntosUser += 1
        # si el resultado es el valor elegido por la maquina, se muestra un mensaje de ronda ganada y se suma un punto la maquina
        else:
            print('has perdido la ronda')
            puntosEnemigo += 1
        # se muestra un resumen de los puntos del usuario y la maquina
        print('Resumen de puntos:')
        print(f'Tu: {puntosUser}')
        print(f'Enemigo: {puntosEnemigo}')
    # si al salir del bucle, el usuario ha ganado 3 veces, se muestra un mensaje de victoria
    if puntosUser > 2:
        print('-------------------------------------------------------')
        print('----------------------- VICTORY -----------------------')
        print('-------------------------------------------------------')
    # si al salir del bucle, la maquina ha ganado 3 veces, se muestra un mensaje de derrota
    elif puntosEnemigo > 2:
        print('-------------------------------------------------------')
        print('---------------------- GAME OVER ----------------------')
        print('-------------------------------------------------------')

def compararEleccion(valorUser, valorEnemigo):
    # comparamos los valores elegidos por el usuario y la maquina
    if (valorUser == 'piedra' and valorEnemigo == 'tijeras') or (valorUser == 'papel' and valorEnemigo == 'piedra') or (valorUser == 'tijeras' and valorEnemigo == 'papel'):
        return valorUser # si el valor elegido por el usuario gana a el de la maquina, se devuelve el valor elegido por el usuario ya que a ganado la ronda
    elif valorUser == valorEnemigo: 
        return "empate" # si el valor elegido por el usuario es igual al de la maquina, se devuelve "empate" ya que a empatado
    else:
        return valorEnemigo # si el valor elegido por el usuario no gana a el de la maquina, se devuelve el valor elegido por la maquina ya que esta a ganado la ronda

def tablero(palabra):
    tablero = ''
    # iteramos sobre cada caracter de la palabra para convertirlo en un String
    for char in palabra:
        tablero += char
    print(tablero.strip())

def ahorcado():
    # obtenemos el directorio actual del programa
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # obtenemos el archivo de palabras mediante su ruta
    csv_file = os.path.join(current_dir, "palabras.csv")
    # creamos una lista vacia para almacenar las palabras del archivo
    palabras = []
    # creamos una lista vacia para almacenar las letras descubiertas por el usuario
    letras_usadas = []
   # abrimos el archivo de palabras mediante el comando "with open"
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            palabras.extend(row)

    # seleccionamos una palabra aleatoria del archivo
    palabraSeleccionada = random.choice(palabras)

    # obtenemos la longitud de la palabra seleccionada
    long = len(palabraSeleccionada)
    # creamos una lista vacia para almacenar las letras de la palabra seleccionada en "_"
    palabra_tablero = ['_'] * long

    # mostramos mensaje de inicio del juego indicando la cantidad de letras que tiene la palabra
    print('------------------------- AHORCADO -------------------------')
    print(f'La palabra a adivinar tiene una longitud de {long} letras, suerte!!')
    intentos = 3
    # entramos en bucle mientras el usuario no haya gastado sus intentos
    while intentos > 0:
        # mostramos el tablero de la palabra con la lista que almacena las posiciones acertadas y las que no con "_"
        tablero(palabra_tablero)
        print(f'Tienes {intentos} intentos para adivinar la palabra')
        # obtenemos la letra del usuario
        letraUser = input('Introduce una letra: ')
        # si la letra del usuario esta en la lista de letras usadas, nos indicara que ya has usado esa letra
        if letraUser in letras_usadas:
            print(f"Ya has usado la letra '{letraUser}'.")
            continue
        # si la letra del usuario esta en la palabra seleccionada, nos indicara que la letra existe en la palabra
        if letraUser in palabraSeleccionada:
            print(f"Bien hecho, la letra '{letraUser}' se encuentra en la palabra.")
            # iteramos sobre cada posicion de la palabra seleccionada y si la letra del usuario es igual a la letra en esa posicion, 
            # se cambia el caracter en la lista de palabra_tablero por la letra del usuario
            for i, valor in enumerate(palabraSeleccionada):
                if valor == letraUser:
                    palabra_tablero[i] = letraUser
            
            if "_" not in palabra_tablero:
                intentos = 0
                continue
        else:
            # si la letra del usuario no esta en la palabra seleccionada, nos indicara que la letra no existe en la palabra
            print(f"La letra {letraUser} no se encuentra en la palabra.")
            intentos -= 1
    
    # si la lista de palabra_tablero no contiene ningun caracter "_", nos indicara que la palabra se ha adivinado 
    if "_" not in palabra_tablero:
        print(f"FELICIDADESS, HAS ACERTADO LA PALABRA")
    # si la lista de palabra_tablero contiene algun caracter "_", nos indicara que la palabra no se ha adivinado
    else:
        print(f"GAME OVER: otra vez sera...")

    # mostramos la palabra
    print(f"La palabra era {palabraSeleccionada}")

def main():
    while True:
        # entramos en bucle y mostramos las opciones al jugador (1-4) siendo 4 la opción para salir del menu.
        print('----------------  MENU GAMEROOM ----------------')
        print('-    1: Adivina el numero.')
        print('-    2: Piedra, papel, tijera.')
        print('-    3: Ahorcado.')
        print('-    4: Salir.-')

        opcionUser = int(input("A que jugamos?(1-4) "))

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
            print("indica un juego valido.") #en el caso de no introducir un valor valido, nos indicara que el valor introducido no es valido.

if __name__ == "__main__":
    main()
