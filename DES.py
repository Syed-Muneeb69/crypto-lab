from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    """Encrypt the plaintext using DES."""
    # Ensure key length is 8 bytes
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long.")
    
    # Initialize DES cipher in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Pad plaintext to be a multiple of 8 bytes
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    
    # Encrypt and return the ciphertext
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    """Decrypt the ciphertext using DES."""
    # Ensure key length is 8 bytes
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long.")
    
    # Initialize DES cipher in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Decrypt and unpad the plaintext
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, DES.block_size).decode()
    return plaintext

# Example usage
if __name__ == "__main__":
    key = b'secret12'  # 8-byte key
    plaintext = "My name is Syed Muneeb"

    # Encrypt the plaintext
    ciphertext = des_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext.hex())

    # Decrypt the ciphertext
    decrypted_text = des_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
