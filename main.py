from cryptography.fernet import Fernet 
import time

def gen_key():
    key = Fernet.generate_key()
    with open('crypt.txt', 'wb') as f:
        f.write(key)


def enc_file():
    filename = str(input("Filename: "))
    with open(filename, 'rb') as file:
        content = file.read()
        with open('crypt.txt', 'rb') as keyfile:
            crypt = Fernet(keyfile.read())
            encrypted_content = crypt.encrypt(content)
            with open(filename, 'wb') as f:
                f.write(encrypted_content)

def decrypt():
    filename = str(input("Filename: "))
    with open(filename, 'rb') as file:
        content = file.read()
    with open('crypt.txt', 'rb') as keyfile:
        crypt = Fernet(keyfile.read())
        decrypted_content = crypt.decrypt(content)
        with open(filename, 'wb') as f:
            f.write(decrypted_content)


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