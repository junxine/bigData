with open("README") as file:
    while True:
        if text := file.readline():
            print(text)

        else:
            break
