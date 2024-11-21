
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                result += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Example usage
plaintext = "hello world"
shift = 3
encrypted_text = caesar_cipher_encrypt(plaintext, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
