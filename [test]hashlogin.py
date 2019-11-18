import getpass
#user = getpass.getpass('Input U password:')
#print (user)
import os, base64
import hashlib
from hmac import HMAC
'''
print (getpass.getuser())
pwd=getpass.getpass('input your password:')
print(pwd)
'''

#écriture dans le fichier
def ecrire():
    while True:
        try:
            nomFichier = str(input("Entrez le nom de fichier du login： "))
            fichier = open(nomFichier, "a")
            fichier.write( str(input("Entrez le login : \n")))
            pwd=str(input("Entrez le mot de pass : \n"))

            encryptpwd=encrypt_password(pwd,salt=None)
            fichier.write("\n" + encryptpwd)
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            fichier.close()
            break


def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8)  # 64 bits.  #ajouter salage

    assert 8 == len(salt)
    assert isinstance(salt, bytes)
    assert isinstance(password, str)

    if isinstance(password, str):
        password = password.encode('UTF-8')

    assert isinstance(password, bytes)

    result = password
    for i in range(10):
        result = HMAC(result, salt, hashlib.sha256).digest()

    return str(salt + result)

def validate_password():
    input_password=input("Entrez le mot de pass : \n")
    hashed="b'{\x063-<\xb2\x16Y\xa2\x92X\x8b\xc7\xa1\xf2\xf3\x17\xb8\xa7\x8e\nGe\x8f\x04\xf8\xfc\x82\xfdTC\xc4|{\xe0\xf50c\xa3\xde'"
    return hashed == encrypt_password(input_password, salt=hashed[:8])



#Création du menu
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
                    ecrire()
                elif choix == 3:
                    if(validate_password()==1):
                        print('yes')
                    else:
                        print('no')
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

