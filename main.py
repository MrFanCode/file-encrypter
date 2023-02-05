from cryptography.fernet import Fernet 

# This function will generate encryption key. The generaed key file is required to encrypt or decrypt a file.
def gen_key():
    key = Fernet.generate_key()
    with open('key.txt', 'wb') as f:
        f.write(key)


# This function will encrypt a file.
def enc_file():
    filename = str(input("Filename: "))
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            with open('key.txt', 'rb') as keyfile:
                crypt = Fernet(keyfile.read())
                encrypted_content = crypt.encrypt(content)
                with open(filename, 'wb') as f:
                    f.write(encrypted_content)
                    print("File has been encrypted.")
    except FileNotFoundError:
        print("File not found. Please check the file location that you enter.")


# This function will decrypt a file.
def decrypt():
    filename = str(input("Filename: "))
    try:
        with open(filename, 'rb') as file:
            content = file.read()
        with open('key.txt', 'rb') as keyfile:
            crypt = Fernet(keyfile.read())
            decrypted_content = crypt.decrypt(content)
            with open(filename, 'wb') as f:
                f.write(decrypted_content)
                print("File has been decrypted.")
    except FileNotFoundError:
        print("File not found. Please check the file name and the location that uou entered.")


def run():
    run = True
    while run:
        command = str(input("Command: "))
        if command == "enc":
            enc_file()
        elif command == "dec":
            decrypt()
        elif command == "gen key":
            gen_key()
        elif command == "exit":
            run = False
        elif command == "help":
            print("""
            COMMANDS:
                1.enc - encrypt
                2.dec - decrypt
                3.gen key - generate key file
                4.help - show this output
                5.exit - to exit
            """)


run()
