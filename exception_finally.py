def run():
    try: 
        f = open("archivo.txt")
        # Hacer cualquier cosa con nuestor archivo
    finally:
        f.close()

if __name__ == "__main__":
    run()