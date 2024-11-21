import string

def generate_cipher_alphabet(key):
    """Generate a cipher alphabet using the provided key."""
    key = "".join(dict.fromkeys(key))  # Remove duplicate letters
    remaining_letters = "".join([ch for ch in string.ascii_lowercase if ch not in key])
    return key + remaining_letters

def encrypt_substitution_cipher(plaintext, key):
    """Encrypt the plaintext using a substitution cipher."""
    cipher_alphabet = generate_cipher_alphabet(key)
    alphabet = string.ascii_lowercase
    cipher_map = str.maketrans(alphabet, cipher_alphabet)
    return plaintext.lower().translate(cipher_map)

def decrypt_substitution_cipher(ciphertext, key):
    """Decrypt the ciphertext using a substitution cipher."""
    cipher_alphabet = generate_cipher_alphabet(key)
    alphabet = string.ascii_lowercase
    decipher_map = str.maketrans(cipher_alphabet, alphabet)
    return ciphertext.lower().translate(decipher_map)

# Example usage
key = "keyword"  # The cipher key
plaintext = "syed muneeb"
ciphertext = encrypt_substitution_cipher(plaintext, key)
decrypted_text = decrypt_substitution_cipher(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
