class spaste:
    def text(content, url='https://www.toptal.com/developers/hastebin'):
        link = internals(content, url)
        print(link)
        return link

    def file(filename, url='https://www.toptal.com/developers/hastebin'):
        from requests import post
        with open(filename) as f:
            lines = f.readlines()
        data = ""
        for i in range(len(lines)):
            data += lines[i]
        internals(data, url)


def internals(content, url):
    from requests import post
    poster = post(f'{url}/documents', data=content.encode('utf-8'))
    link = f'{url}/{poster.json()["key"]}'
    return link