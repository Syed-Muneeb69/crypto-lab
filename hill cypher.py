import numpy as np

def mod_inverse(a, m):
    """Calculate the modular inverse of a under modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Modular inverse does not exist for {a} under modulo {m}.")

def encrypt_hill_cipher(plaintext, key_matrix):
    """Encrypt the plaintext using the Hill cipher."""
    plaintext = plaintext.lower().replace(" ", "")
    while len(plaintext) % 2 != 0:  # Pad with 'x' if the plaintext length is odd
        plaintext += 'x'
    
    key_matrix = np.array(key_matrix)
    encrypted_text = ""
    
    for i in range(0, len(plaintext), 2):
        block = [ord(plaintext[i]) - ord('a'), ord(plaintext[i + 1]) - ord('a')]
        result = np.dot(key_matrix, block) % 26
        encrypted_text += ''.join(chr(num + ord('a')) for num in result)
    
    return encrypted_text

def decrypt_hill_cipher(ciphertext, key_matrix):
    """Decrypt the ciphertext using the Hill cipher."""
    ciphertext = ciphertext.lower().replace(" ", "")
    key_matrix = np.array(key_matrix)
    
    # Calculate the determinant and modular inverse
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26
    determinant_inverse = mod_inverse(determinant, 26)
    
    # Calculate the adjugate and modular inverse of the key matrix
    adjugate = np.linalg.inv(key_matrix).T * determinant
    key_inverse = (determinant_inverse * adjugate) % 26
    key_inverse = np.round(key_inverse).astype(int) % 26
    
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        block = [ord(ciphertext[i]) - ord('a'), ord(ciphertext[i + 1]) - ord('a')]
        result = np.dot(key_inverse, block) % 26
        decrypted_text += ''.join(chr(num + ord('a')) for num in result)
    
    return decrypted_text

# Example usage
key_matrix = [[3, 3], [2, 5]]  # Example key matrix
plaintext = "My name is Muneeb"
ciphertext = encrypt_hill_cipher(plaintext, key_matrix)
decrypted_text = decrypt_hill_cipher(ciphertext, key_matrix)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
