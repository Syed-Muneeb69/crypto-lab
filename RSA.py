from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes


def generate_rsa_keys():
key = RSA.generate(2048) private_key = key.export_key()
public_key = key.publickey().export_key() return private_key, public_key

def rsa_encrypt(text, public_key): rsa_public_key = RSA.import_key(public_key)
cipher_rsa = PKCS1_OAEP.new(rsa_public_key) encrypted_text = cipher_rsa.encrypt(text.encode()) return encrypted_text

def rsa_decrypt(encrypted_text, private_key): rsa_private_key = RSA.import_key(private_key) cipher_rsa = PKCS1_OAEP.new(rsa_private_key)
decrypted_text = cipher_rsa.decrypt(encrypted_text).decode() return decrypted_text

Example usage
private_key, public_key = generate_rsa_keys() plaintext = "hello"
encrypted_text = rsa_encrypt(plaintext, public_key)
decrypted_text = rsa_decrypt(encrypted_text, private_key)
 


print("Plaintext:", plaintext) print("Encrypted:", encrypted_text) print("Decrypted:", decrypted_text)



