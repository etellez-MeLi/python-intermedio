
def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Eduardo", "lastname": "Tellez"}

    super_list = [
        {"firstname": "Eduardo", "lastname": "Tellez"},
        {"firstname": "Raúl", "lastname": "Crisostomo"},
        {"firstname": "Rubén", "lastname": "González"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)


# Entry point, inicializa la función cuando corremos el archivo
if __name__ == "__main__":
    run()