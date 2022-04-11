class sfile:

    def send(url, filepath, key):
        from .paste import spaste

        send_data(url, filepath.split("\\")[-1], spaste.file(filepath))

    def receive(key):
        if key is None:
            from threading import Thread

            thread_data = Thread(target=receive_data)
            return thread_data
        else:
            from threading import Thread

            thread_data = Thread(target=receive_data_key, args=(key, ))
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

    from .paste import spaste

    app = flask.Flask(__name__)

    @app.route("/", methods=["POST"])
    def server():
        url = flask.request.form["url"]
        filepath = flask.request.form["filename"]
        spaste.save(url, filepath)
        return "Request Complete"

    app.run(host="0.0.0.0")


def receive_data_key(key):
    import flask

    from .paste import spaste

    app = flask.Flask(__name__)

    @app.route("/", methods=["POST"])
    def server():
        url = flask.request.form["url"]
        filepath = flask.request.form["filename"]
        sentkey = flask.request.form["key"]
        if sentkey == key:
            spaste.save(url, filepath)
            return "Request Complete"
        else:
            return "Key incorrect"

    app.run(host="0.0.0.0")
