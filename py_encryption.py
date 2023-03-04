from cryptography.fernet import Fernet

import os
import pickle
import time

# Decrypt text using the command line
def decrypt(text, key):
    f = Fernet(key)
    data_unencrypted = f.decrypt(text)
    data_unencrypted = data_unencrypted.decode('utf-8')
    return data_unencrypted

# Decrypt a file containing text
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

# Encrypt text using the command line
def encrypt(text, key):
    f = Fernet(key)
    text = bytes(text, 'utf-8')
    data_encrypted = f.encrypt(text)
    return data_encrypted

# Encrypt a file containing text
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# Generate a new key
def gen_key(filename):
    key = Fernet.generate_key()
    filename = filename + '.pk'
    with open(filename, 'wb') as x:
        pickle.dump(key, x)

# Load a key for encryption or decryption
def load_key(filename):
    with open(filename, 'rb') as x:
        key = pickle.load(x)
    return key

if __name__ == '__main__':

    # Create a loop for the program to run continuously
    running = True
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')
        # First menu
        user_choice_init = int(input('1. Load Key\n2. Generate New Key \n3. Stop Program\nSelection (1/2/3): '))
        if user_choice_init == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            filename = input('Name of file containing key: ')
            key = load_key(filename)
            # Create a loop for second menu to run continuously
            running1 = True
            while running1:
                os.system('cls' if os.name == 'nt' else 'clear')
                # Second menu
                user_choice = int(input('1. Encrypt Input\n2. Decrypt Input\n3. Encrypt File\n4. Decrypt File\n5. Stop Program\n6. Back\nSelection (1/2/3/4/5/6): '))
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
                    filepath = input('Enter Name of File: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    encrypt_file(filepath, key)
                    print(f'{filepath} Encrypted...')
                    time.sleep(2)
                elif user_choice == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    filepath  = input('Enter Name of File: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    decrypt_file(filepath, key)
                    print(f'{filepath} decrypted...')
                    time.sleep(2)
                elif user_choice == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Stopping Encryption Program...')
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    running1 = False
                    running = False
                elif user_choice == 6:
                    running1 = False
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
        
        


