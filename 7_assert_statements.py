def divisors(num):
    divisors = []
    for i in range(1, num + 1) :
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingresa un número: ")

    # if int(num) <= 0:
    #     raise ValueError("Debes ingresar un número positivo")
    ## assert it's almost the same as try-except, just another way, you need to compare first
    ## if num >= 0 because u are comparing string now
    assert int(num) >= 0, "Debes ingresar un numero positivo"

    # isnumeric es método para las cadenas de caracteres
    assert num.isnumeric(), "Debes ingresar un número"

    print(divisors(int(num)))
    print("Terminó mi programa")

if __name__ == '__main__':
    run()