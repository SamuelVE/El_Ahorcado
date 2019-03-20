def attempt_0():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |                  ")
    print(" |                  ")
    print(" |                  ")
    print(" |                  ")
    print(" |                  ")
    print("----                ")


def attempt_1():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |           ( )    ")
    print(" |                  ")
    print(" |                  ")
    print(" |                  ")
    print(" |                  ")
    print("----                ")


def attempt_2():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |           ( )    ")
    print(" |            |     ")
    print(" |            |     ")
    print(" |                  ")
    print(" |                  ")
    print("----                ")


def attempt_3():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |           ( )    ")
    print(" |            |     ")
    print(" |            |     ")
    print(" |           /      ")
    print(" |          /       ")
    print("----                ")


def attempt_4():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |           ( )    ")
    print(" |            |     ")
    print(" |            |     ")
    print(" |           / \\   ")
    print(" |          /   \\  ")
    print("----                ")


def attempt_5():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |           ( )    ")
    print(" |           /|     ")
    print(" |          / |     ")
    print(" |           / \\   ")
    print(" |          /   \\  ")
    print("----                ")


def attempt_6():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |           ( )    ")
    print(" |           /|\\  ")
    print(" |          / | \\ ")
    print(" |           / \\   ")
    print(" |          /   \\  ")
    print("----                ")


def attempt_7():
    print(" |-------------     ")
    print(" |            |     ")
    print(" |          _( )_   ")
    print(" |           /|\\   ")
    print(" |          / | \\  ")
    print(" |           / \\   ")
    print(" |          /   \\  ")
    print("----                ")


def winner():
    print(" |                  ")
    print(" |                  ")
    print(" |          (^u^)   ")
    print(" |           /|\\   ")
    print(" |          / | \\  ")
    print(" |           / \\   ")
    print(" |          /   \\  ")
    print("----                ")


def get_attempt( difficulty, lifes ):
    if difficulty == "1":  #NIVEL FÁCIL
        if lifes == 7:
            attempt_0()
        elif lifes == 6:
            attempt_1()
        elif lifes == 5:
            attempt_2()
        elif lifes == 4:
            attempt_3()
        elif lifes == 3:
            attempt_4()
        elif lifes == 2:
            attempt_5()
        elif lifes == 1:
            attempt_6()
        elif lifes == 0:
            attempt_7()
    elif difficulty == "2":  #NIVEL MEDIO
        if lifes == 5:
            attempt_0()
        elif lifes == 4:
            attempt_1()
        elif lifes == 3:
            attempt_2()
        elif lifes == 2:
            attempt_4()
        elif lifes == 1:
            attempt_6()
        elif lifes == 0:
            attempt_7()
    elif difficulty == "3":  #NIVEL DIFICIL
        if lifes == 3:
            attempt_0()
        elif lifes == 2:
            attempt_2()
        elif lifes == 1:
            attempt_6()
        elif lifes == 0:
            attempt_7()
