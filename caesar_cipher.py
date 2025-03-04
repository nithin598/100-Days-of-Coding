import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(f'{art.logo}')

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def caesar(original_text,shift_amount):
    cipher_string = ''
    if direction == 'decode':
        shift_amount *= -1
    for char in original_text:
        new_shift = 0
        if char in alphabet:
            new_shift = shift_amount + alphabet.index(char)
            new_shift %= 26
            new_char=alphabet[new_shift]
        else:
            new_char = char
        cipher_string += new_char
    print(cipher_string)

restart = 'yes'
while  restart=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,2)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

