import numpy as np

def mod_inverse(a, m):
    """Calculate the modular inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Modular inverse does not exist for {a} under modulo {m}.")

def encrypt_hill_cipher(plaintext, key_matrix):
    """Encrypt the plaintext using the Hill cipher."""
    plaintext = plaintext.lower().replace(" ", "")
    while len(plaintext) % len(key_matrix) != 0:  # Pad with 'x' if plaintext length is not divisible by matrix size
        plaintext += 'x'
    
    key_matrix = np.array(key_matrix)
    encrypted_text = ""
    
    for i in range(0, len(plaintext), len(key_matrix)):
        block = [ord(char) - ord('a') for char in plaintext[i:i + len(key_matrix)]]
        result = np.dot(key_matrix, block) % 26
        encrypted_text += ''.join(chr(num + ord('a')) for num in result)
    
    return encrypted_text

def decrypt_hill_cipher(ciphertext, key_matrix):
    """Decrypt the ciphertext using the Hill cipher."""
    ciphertext = ciphertext.lower().replace(" ", "")
    key_matrix = np.array(key_matrix)
    
    # Calculate the determinant and modular inverse
    determinant = int(round(np.linalg.det(key_matrix))) % 26
    if determinant == 0:
        raise ValueError("Key matrix is not invertible under modulo 26.")
    determinant_inverse = mod_inverse(determinant, 26)
    
    # Calculate the adjugate (cofactor transpose)
    cofactors = np.zeros_like(key_matrix)
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            minor = np.delete(np.delete(key_matrix, i, axis=0), j, axis=1)
            cofactors[i, j] = int(round(np.linalg.det(minor))) * ((-1) ** (i + j))
    adjugate = cofactors.T % 26
    
    # Compute the modular inverse of the key matrix
    key_inverse = (determinant_inverse * adjugate) % 26
    
    decrypted_text = ""
    for i in range(0, len(ciphertext), len(key_matrix)):
        block = [ord(char) - ord('a') for char in ciphertext[i:i + len(key_matrix)]]
        result = np.dot(key_inverse, block) % 26
        decrypted_text += ''.join(chr(num + ord('a')) for num in result)
    
    return decrypted_text.rstrip('x')  # Remove padding

# Example usage
key_matrix = [[3, 3], [2, 5]]  # Example key matrix
plaintext = "mynameismuneeb"
ciphertext = encrypt_hill_cipher(plaintext, key_matrix)
decrypted_text = decrypt_hill_cipher(ciphertext, key_matrix)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
