alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

text = input("Type your maeeage: ").lower()
shift = int(input("Type the shift number:  "))

# Encryption
def encrypt(original_text, shift_num):
    encrypted_message = ''
    for letter in original_text:
        encrypt_index = (alphabet.index(letter) + shift_num) % len(alphabet)
        encrypted_message += alphabet[encrypt_index]

    print(encrypted_message)




# Decryption
def decrypt(encrypted_message, shift_num):
    decrypted_message = ''
    for letter in encrypted_message:
        decrypt_index = (alphabet.index(letter) - shift_num) % len(alphabet)
        decrypted_message += alphabet[decrypt_index]

    print(decrypted_message)



if direction == 'encrypt':
    encrypt(text, shift)
else:
    decrypt(text, shift)

