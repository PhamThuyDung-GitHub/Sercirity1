def vigenere_encrypt(text, key):
    encrypted_text = ""
    extended_key = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            extended_key += key[key_index % key_length]
            key_index += 1
        else:
            extended_key += char

    for i in range(len(text)):
        char = text[i]
        shift = ord(extended_key[i]) - ord('A')
        
        if char.isalpha():  # Encrypt only alphabets
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += char
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    extended_key = ""
    key_length = len(key)
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            extended_key += key[key_index % key_length]
            key_index += 1
        else:
            extended_key += char

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        shift = ord(extended_key[i]) - ord('A')
        
        if char.isalpha():  # Decrypt only alphabets
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += char
        else:
            decrypted_text += char

    return decrypted_text

if __name__ == "__main__":
    mode = input("Choose mode (encrypt/decrypt): ").upper()
    message = input("Enter the message: ").upper()  # Convert message to uppercase
    key = input("Enter the key: ").upper()  # Convert key to uppercase
    
    if mode == "ENCRYPT":
        print(vigenere_encrypt(message, key))
    elif mode == "DECRYPT":
        print(vigenere_decrypt(message, key))
    else:
        print("Invalid mode selected.")
