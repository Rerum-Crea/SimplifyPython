class spaste:

    def text(content, url="https://www.toptal.com/developers/hastebin"):
        link = write_internals(content, url)
        print(link)
        return link

    def file(filename, url="https://www.toptal.com/developers/hastebin"):
        data = stitch(filename)
        link = write_internals(data, url)
        print(link)
        return link

    def read(url):
        from requests import get
        data = get(url)
        content = data.text
        print(content)
        return content



def write_internals(content, url):
    from requests import post

    poster = post(f"{url}/documents", data=content.encode("utf-8"))
    link = f'{url}/{poster.json()["key"]}'
    return link


def stitch(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = ""
    for i in range(len(lines)):
        data += lines[i]
    return data
