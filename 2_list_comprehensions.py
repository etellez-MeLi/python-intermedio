def run():
    squares = []

    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    # El cuadrado de los numeros que no sean divisibles entre 3
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)

    # Numeros multiplos de 4, 6 y 9 de hasta 5 digitos
    multiplos = [ i for i in range (1, 99999) if i%4 == 0 and i%6 == 0 and i%9 == 0 ]
    print(multiplos)


if __name__ == '__main__':
    run()