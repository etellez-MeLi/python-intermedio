def run():

    # diccionario de keys 100 primeros num naturales y values sea el cubo
    dict_naturales = { i:i**3 for i in range(1,101) if i%3 != 0}
    # print(dict_naturales)

    sqrt = { i : i**(1/2) for i in range(1,1001)}
    print(sqrt)

if __name__ == "__main__":
    run()