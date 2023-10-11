def encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force(cipher_text):
    for key in range(1, 26):
        print(f"Key {key}: {decrypt(cipher_text, key)}\n")

def main():
    option = input("Choose an option (encrypt, decrypt, brute_force): ")
    if option == "encrypt":
        key = int(input("Enter the key (0-25): "))
        plain_text = input("Enter the plaintext: ")
        print(f"Ciphertext: {encrypt(plain_text, key)}")
    elif option == "decrypt":
        key = int(input("Enter the key (0-25): "))
        cipher_text = input("Enter the ciphertext: ")
        print(f"Plaintext: {decrypt(cipher_text, key)}")
    elif option == "brute_force":
        cipher_text = input("Enter the ciphertext: ")
        brute_force(cipher_text)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
