import getpass


def enregistrer():
    while True:
        try:
            nomFichier = str(input("Entrez le nom de fichier du login： "))
            fichier = open(nomFichier, "a")
            fichier.write( str(input("Entrez le login : \n")))
            pwd=getpass.getpass("Entrez le mot de pass : \n")
            fichier.write("\n" + pwd)
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            fichier.close()
            break

def verifier():
    while True:
        try:
            input_login = str(input("Entrez le login : \n"))
            input_password = getpass.getpass("Entrez le mot de pass : \n")

            fichier = open('login.txt', "r")
            lines = fichier.readlines()
            lines[0]=lines[0].strip('\n')
            lines[1]=lines[1].strip('\n')

            if input_login==lines[0] and input_password==lines[1]:
                print("login successful")
            else:
                print("login fialed")

        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            fichier.close()
            break

def main():
    print("2. Enregistrer le mot de passe")
    print('3. Vérifier le mot de passe')
    print("9. Quitter")

    choix = 0

    while choix != 9:

        while True:
            try:
                choix = int(input("Entrez votre choix : "))
                if choix == 2:
                    enregistrer()
                elif choix == 3:
                    verifier()
                elif choix == 9:
                    exit()
                else:
                    print("Choix non valide!")
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again   ")
            finally:
                print("------------------")


if __name__ == '__main__':
    main()