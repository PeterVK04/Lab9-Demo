#Encoder Peter Van Kirk
def encoder(password):
    result = ''
    for i in range(len(password)):
        result += str((int(password[i]) + 3) % 10)
    return result

# decryption function

def main():
    print('Menu' +
    '\n -------------')

    print(' 1. Encode' +
          '\n 2. Decode' +
          '\n 3.Quit')

    while True:
        print('Please enter an option: ')
        choice = int(input(''))
        if choice == 1:
            password = input('Please enter your passweord to encode: ')
            encodedPassword = encoder(password)
        if choice == 3:
            return


if __name__ == '__main__':
    main()