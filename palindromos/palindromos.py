def verif_palindromo ():
    palindromo= str.split(str.lower(input("ingrese palindromo: ")))
    palindromo_espacios= "".join(palindromo)
    palindromo_verif= palindromo_espacios[::-1]
    if palindromo_espacios==palindromo_verif:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

verif_palindromo ()
