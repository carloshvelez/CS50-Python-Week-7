import validators

def main():

    if validar(input("Ingrese su correo electrónico: ")):
        print ("Valid")

    else:
        print("Invalid")


def validar(mail):
    return validators.email(mail)



if __name__ == "__main__":
    main()