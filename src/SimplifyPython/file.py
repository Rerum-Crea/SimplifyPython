class sfile:
    def send(url, filepath, key=None):
        if key is None:
            from .paste import spaste

            new_filepath = create_temp(filepath)
            send_data(url, new_filepath.split("\\")[-1], spaste.file(new_filepath)) # .tpm given
        else:
            from .paste import spaste
            from .crypto import scrypto

            new_filepath = scrypto.encrypt_file(scrypto.generate_key('', b''), filepath)
            send_data_key(url,
                          filepath.split("\\")[-1], spaste.file(new_filepath), key)

    def send_encrypted(url, filepath, key):
        from .crypto import scrypto
        from .paste import spaste

        new_filepath = scrypto.encrypt_file(key, filepath)
        send_data(url,
                      new_filepath.split("\\")[-1], spaste.file(new_filepath))

    def receive(key=None, daemon=False):
        if key is None:
            from threading import Thread

            thread_data = Thread(target=receive_data, daemon=daemon)
            return thread_data
        else:
            from threading import Thread

            thread_data = Thread(target=receive_data_key, args=(key, ), daemon=daemon)
            return thread_data

    def receive_encrypted(key, daemon=False):
        from threading import Thread

        thread_data = Thread(target=receive_data_encrypted, args=(key, ), daemon=daemon)
        return thread_data


def send_data(url, filename, pasteurl):
    import requests

    data = {"url": pasteurl, "filename": filename, "key": None}
    r = requests.post(url, data=data)
    print(r.text)


def send_data_key(url, filename, pasteurl, key):
    import requests

    data = {"url": pasteurl, "filename": filename, "key": key}
    r = requests.post(url, data=data)
    print(r.text)


def receive_data():
    import flask
    import os
    from .paste import spaste
    from .crypto import scrypto

    app = flask.Flask(__name__)

    @app.route("/", methods=["POST"])
    def server():
        url = flask.request.form["url"]
        filepath = flask.request.form["filename"]
        spaste.save(url, filepath)
        scrypto.decrypt_file(b'ZKho1LI69pbTc00LgU0EzdGsKAEo6XZToF8ytJwTopo=', filepath)
        os.remove(filepath)
        return "Request Complete"

    app.run(host="0.0.0.0")


def receive_data_key(key):
    import flask
    import os
    from .paste import spaste
    from .crypto import scrypto

    app = flask.Flask(__name__)

    @app.route("/", methods=["POST"])
    def server():
        url = flask.request.form["url"]
        filepath = flask.request.form["filename"]
        sentkey = flask.request.form["key"]
        if sentkey == key:
            spaste.save(url, filepath)
            scrypto.decrypt_file(b'ZKho1LI69pbTc00LgU0EzdGsKAEo6XZToF8ytJwTopo=', filepath)
            os.remove(filepath)
            return "Request Complete"
        else:
            return "Key incorrect"

    app.run(host="0.0.0.0")


def receive_data_encrypted(key):
    import os

    import flask

    from .crypto import scrypto
    from .paste import spaste

    app = flask.Flask(__name__)

    @app.route("/", methods=["POST"])
    def server():
        url = flask.request.form["url"]
        filepath = flask.request.form["filename"]
        spaste.save(url, filepath)
        scrypto.decrypt_file(key, filepath)
        os.remove(filepath)
        return "Request Complete"

    app.run(host="0.0.0.0")


def stitch(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = ""
    for i in range(len(lines)):
        data += lines[i]
    return data

def create_temp(filepath):
    from cryptography.fernet import Fernet
    from .crypto import scrypto
    with open(filepath, "rb") as f:
        data = f.read()
    outfile = f"{filepath}.tmp"
    key = scrypto.generate_key('', b'')
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(outfile, "wb") as f:
        f.write(encrypted)
    return outfile
