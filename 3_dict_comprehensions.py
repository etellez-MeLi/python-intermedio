def run():

    # diccionario de keys 100 primeros num naturales y values sea el cubo
    
    dict_naturales = { i:i**3 for i in range(1,101) }
    print(dict_naturales)

if __name__ == "__main__":
    run()