def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No puedes dejar el espacio en blanco")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try: 
    print(palindrome(""))
except TypeError:
    print("Solo se puede ingresar texto") 

if __name__ == "__main__":
    palindrome()