from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Key Pair Generation
key = RSA.generate(2048)  # 2048-bit key
private_key = key.export_key()  # Export private key
public_key = key.publickey().export_key()  # Export public key

print("Private Key:")
print(private_key.decode())
print("\nPublic Key:")
print(public_key.decode())

# Message to encrypt
message = b"Muneeb"

# Encryption
public_key_obj = RSA.import_key(public_key)
cipher = PKCS1_OAEP.new(public_key_obj)  # RSA with OAEP padding
ciphertext = cipher.encrypt(message)

print("\nCiphertext (hex):")
print(ciphertext.hex())

# Decryption
private_key_obj = RSA.import_key(private_key)
decipher = PKCS1_OAEP.new(private_key_obj)
plaintext = decipher.decrypt(ciphertext)

print("\nDecrypted message:")
print(plaintext.decode())
