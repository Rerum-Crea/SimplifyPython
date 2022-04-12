from time import sleep

from SimplifyPython import scrypto

key = scrypto.generate_key('password', b'12345')

encrypted_message = scrypto.encrypt(key, 'hello, world')

print(encrypted_message)

decrypted_message = scrypto.decrypt(key, encrypted_message)

print(decrypted_message)

scrypto.decrypt_file(key, 'data.json.encrypted')
