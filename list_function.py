def run():
    my_list = [1,5,63,48,52,99,72,45,16,33,78,34,26,55,11,33]
    odd = list(filter(lambda x: x%2 !=0, my_list))
    print(odd)

if __name__ == "__main__":
    run()