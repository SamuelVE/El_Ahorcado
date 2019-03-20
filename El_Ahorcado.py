import Stages

wrong_guessed = []
correct_ones = 0
print("------------------EL AHORCADO------------- ")
print("*Patente pendiente por Samuel Vera 2019    ")
print("ingrese la dificultad:                     ")
print("(1) FÁCIL       (2) MEDIO       (3) DIFÍCIL")

difficulty = input(">>")

if difficulty == "1":
    lifes = 7
elif difficulty == "2":
    lifes = 5
elif difficulty == "3":
    lifes = 3

print("Ingrese la palabra a adivinar")
secret_word = input(">>")
lenght = len(secret_word)
guessed = ["_"] * lenght

while lifes != 0:
    print("Vidas: " + str(lifes))  #imprime las vidas restantes
    print(" ".join(wrong_guessed))  #muestra las letras que ya han sido introducidas
    Stages.get_attempt(difficulty, lifes)  #muestra las etapas del ahorcado
    print("Adivina una letra")
    guess = input(">> "+" ".join(guessed))

    # -------------------------------------camino positivo
    if guess in secret_word and guess not in guessed:
        print("muy bien")
        correct_ones += 1
        index = secret_word.index(guess)
        guessed[index] = guess
        if correct_ones == lenght:  # si gana
            print(" ".join(guessed))
            print("Ganaste el juego chingüengüencha!")
            Stages.winner()
            break
    elif guess not in secret_word:
        lifes -= 1
        wrong_guessed.append(guess)
        print("letra incorrecta")
    # --------------------------------------------------------camino negativo

    else:
        print("esa letra ya la dijiste")

if lifes == 0:  # si pierde
    Stages.attempt_7()
    print("la palabra era " + secret_word)
    print("se acabó el juego")
