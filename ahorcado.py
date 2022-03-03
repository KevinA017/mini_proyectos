from ast import Break
import random
import os
def new_game():
    while True:
        try:
            new_game = int(input("""
            Desea jugar de nuevo?
                Pulse 1 para SI.
                Pulse 2 para NO.
                    """))
            break
        except:
            os.system("clear")
            print("SOLO SE PERMITEN NUMEROS\n Intente de nuevo")
    if new_game == 1:
        run()
    else:
        exit()
def read():
    with open("./data.txt", "r") as palabras:
        list_words = [line.replace("\n", "") for line in palabras]
    return list_words

def run():

    while True:
        
        palabra = list(random.choice(read()))
        intentos = 8
        spaces = "_" * len(palabra)
        while intentos > 0:
            os.system("clear")
            print("|{:<20}|".format(f"Tus intentos son: {intentos}"))
            print("\n\nAdivine la siguiente palabra: ")
            print(spaces)
            letra = str(input("Digite una letra: "))
            if letra in palabra:
                for i, a in enumerate(palabra):
                    if letra == a:
                        spaces = list(spaces)
                        spaces[i] = letra
                        spaces = "".join(spaces)
            else:
                intentos -= 1
            encontrar = "".join(palabra)
            if spaces == encontrar:
                os.system("clear")
                print(f"La palabra es {encontrar.upper()}")
                print("GANASTEEEE")
                new_game()
        else:
            os.system("clear")
            print(f"La palabra era: {encontrar.upper()}")
            print("Sigue intentadolo:))")
            new_game()
           

if __name__ == "__main__":
    run()
