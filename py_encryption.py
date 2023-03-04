from cryptography.fernet import Fernet

import os
import pickle
import time

def decrypt(text, key):
    f = Fernet(key)
    data_unencrypted = f.decrypt(text)
    data_unencrypted = data_unencrypted.decode('utf-8')
    return data_unencrypted

def encrypt(text, key):
    f = Fernet(key)
    text = bytes(text, 'utf-8')
    data_encrypted = f.encrypt(text)
    return data_encrypted

def gen_key(filename):
    key = Fernet.generate_key()
    filename = filename + '.pk'
    with open(filename, 'wb') as x:
        pickle.dump(key, x)

def load_key(filename):
    with open(filename, 'rb') as x:
        key = pickle.load(x)
    return key

if __name__ == '__main__':

    running = True
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')
        user_choice_init = int(input('1. Load Key\n2. Generate New Key \n3. Stop Program\nSelection (1/2/3): '))
        if user_choice_init == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            filename = input('Name of file containing key: ')
            key = load_key(filename)
            running1 = True
            while running1:
                os.system('cls' if os.name == 'nt' else 'clear')
                user_choice = int(input('1. Encrypt\n2. Decrypt\n3. Stop Program\nSelection (1/2/3): '))
                if user_choice == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    text = input('Text you want to encrypt: \n')
                    data_encrypted = encrypt(text, key)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    data_encrypted = data_encrypted.decode('utf-8')
                    print(f'\ndata_encrypted: {data_encrypted}')
                    check = input('\nContinue with Loaded Key? (y/n): ')
                    if check == 'n':
                        running1 = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif user_choice == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    text = input('Bytes you want to decrypt: \n')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    data_unencrypted = decrypt(text, key)
                    print(f'data_unencrypted: {data_unencrypted}')
                    check = input('\nContinue with Loaded Key? (y/n): ')
                    if check == 'n':
                        running1 = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif user_choice == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Stopping Encryption Program...')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    running1 = False
                    running = False
                else:
                    print('Invalid Option Selected')
        elif user_choice_init == 2:
            filename = input('Dont add an extension.\nEnter filename for key:\n')
            gen_key(filename)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Key: {filename} Generated...')
            time.sleep(3)
        elif user_choice_init == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            running = False
        else:
            print('Error: Invalid Input')
        # Clear the console
        # os.system('cls' if os.name == 'nt' else 'clear')
        
        


