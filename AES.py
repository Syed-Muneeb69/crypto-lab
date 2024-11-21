from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Key and data setup
key = get_random_bytes(16)  # AES requires key sizes of 16, 24, or 32 bytes
data = b"My name is Syed Muneeb"

# Encryption
cipher = AES.new(key, AES.MODE_CBC)  # CBC mode
ciphertext = cipher.encrypt(pad(data, AES.block_size))  # Padding the data to fit block size

# Decryption
decipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)  # Use the same IV
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

# Output
print(f"Original Data: {data}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Decrypted Data: {plaintext}")
