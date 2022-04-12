class spaste:

    def text(content,
             url="https://www.toptal.com/developers/hastebin",
             doprint=True):
        link = write_internals(content, url)
        if doprint:
            print(link)
        return link

    def file(filename,
             url="https://www.toptal.com/developers/hastebin",
             doprint=True):
        data = stitch(filename)
        link = write_internals(data, url)
        if doprint:
            print(link)
        return link

    def read(url):
        purl = split(url)
        print(read_internals(purl))
        return read_internals(purl)

    def save(url, filename="output.txt"):
        purl = split(url)
        file = open(filename, "w")
        file.write(read_internals(purl))
        file.close()
        return True


def write_internals(content, url):
    from requests import post

    poster = post(f"{url}/documents", data=content.decode())
    link = f'{url}/{poster.json()["key"]}'
    return link


def read_internals(url):
    from requests import get

    data = get(url)
    content = data.text
    return content


def stitch(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    #data = ""
    #for i in range(len(lines)):
        #data += str(lines[i])
    return data


def split(url):
    if "/raw/" in url:
        return url
    else:
        split = url.split("n/")
        try:
            url = f"{split[0]}n/raw/{split[1]}"
            return url
        except KeyError:
            from .print import sprint

            sprint.red(
                "KeyError occurred the url needs to be a hastebin url if it is try removing the slash at "
                "the end if this does not fix it please create an issue at "
                "https://github.com/Necrownyx/SimplifyPython")
            return False
