def hex():
    while True:
        alphabet = input("Enter a character : ")
        if alphabet.isalpha():
            ch = int(alphabet,16)
            return ch
hex()