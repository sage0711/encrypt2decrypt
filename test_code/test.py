from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from save_and_load import *

def generate_key_pair():
    # Generate public and private keys
    key = RSA.generate(2048)

    # Get public and private keys in PEM format
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    return private_key, public_key

def encrypt_data(data, public_key):
    # Encrypt a message using the recipient's public key
    recipient_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(recipient_key)
    encrypted_data = cipher.encrypt(data)

    return encrypted_data

def decrypt_data(data, private_key):
    # Decrypt the message using our private key
    key = RSA.import_key(private_key)
    decryptor = PKCS1_OAEP.new(key)
    decrypted_data = decryptor.decrypt(data)

    return decrypted_data


# Load data from file
load_path = 'text.txt'
data = load_file(load_path)

# Generate key pair
private_key, public_key = generate_key_pair()

# Encrypt data using public key
encrypted_data = encrypt_data(data.encode(), public_key)

# Save encrypted data to file
save_path = 'output.txt'
save_file(save_path, encrypted_data)

# Load encrypted data from file
encrypted_data = load_file(save_path)

# Decrypt data using private key
decrypted_data = decrypt_data(encrypted_data, private_key)

# Save decrypted data to file
save_path = 'output2.txt'
save_file(save_path, decrypted_data)















#from encrypt_and_decrypt import *
#from save_and_load import *
#load_path = 'text.txt'
#save_path = 'output.txt'
#key = 'RRR'
#data = list_encrypt(load_file(load_path), key)
## print(data)
#save_file(save_path, data)
#data2 = list_decrypt(load_file(save_path), key)
## print(data2)
#save_file('out2.txt', data2)