def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict =  {"firstname": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname":"Pedro", "lastname":"Perez"},
        {"firstname":"Maria", "lastname":"Contreras"},
        {"firstname":"Fabiana", "lastname":"Sanchez"},
        {"firstname":"Cristal", "lastname":"Waters"},
        {"firstname":"Gabriel", "lastname":"Ocaña"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for value in super_list:
        print(value)

if __name__ == "__main__":
    run()