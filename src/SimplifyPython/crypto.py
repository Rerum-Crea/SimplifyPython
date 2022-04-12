class scrypto:
    import os

    def generate_key(password_provided, salt=os.urandom(16)):
        import base64

        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

        password = password_provided.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend(),
        )
        key = base64.urlsafe_b64encode(
            kdf.derive(password))  # Can only use kdf once
        return key

    def encrypt(key, input):
        from cryptography.fernet import Fernet

        message = input.encode()
        f = Fernet(key)
        encrypted = f.encrypt(message)
        return encrypted

    def decrypt(key, input):
        from cryptography.fernet import Fernet

        f = Fernet(key)
        decrypted = f.decrypt(input).decode()
        return decrypted

    def encrypt_file(key, filepath=str):
        from cryptography.fernet import Fernet

        with open(filepath, "rb") as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        outfile = f"{filepath}.encrypted"
        with open(outfile, "wb") as f:
            f.write(encrypted)
        return outfile

    def decrypt_file(key, filepath):
        from cryptography.fernet import Fernet, InvalidToken

        split = filepath.split(".")
        split.remove(split[-1])
        output_file = split[0]
        for i in range(len(split)):
            if i != 0:
                output_file += f".{split[i]}"
        with open(filepath, "rb") as f:
            data = f.read()
        fernet = Fernet(key)
        try:
            decrypted = fernet.decrypt(data)
            with open(output_file, "wb") as f:
                f.write(decrypted)
            return output_file
        except InvalidToken as e:
            print("Invalid Key - Unsuccessfully decrypted")
