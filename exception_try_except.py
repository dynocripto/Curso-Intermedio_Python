def palindrome(string):
    return string == string[::-1]

try:
    print(palindrome(1))
except TypeError:
    print("Solo se puede ingresar texto") 
else:
    print("No ocurrió ninguna excepción")

if __name__ == "__main__":
    palindrome()