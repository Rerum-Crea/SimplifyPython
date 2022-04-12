import easygui
from SimplifyPython import sfile

def main():
    filepath = easygui.fileopenbox()
    # sfile.send_encrypted('https://Messin.necrownyx.repl.co', filepath, b'qUVKJy_nN8H8TUSkhbC2X7WjfX7jm51BhD_KbjUwkZw=')
    sfile.send('https://Messin.necrownyx.repl.co', filepath)

main()

def decrypt_file(filepath):

    split = filepath.split(".")
    split.remove(split[-1])
    output_file = split[0]
    for i in range(len(split)):
        if i != 0:
            output_file += f".{split[i]}"
    print(output_file)

def create_temp(filepath):
    outfile = f"{filepath}.tmp"
    print(outfile)
    return outfile

name = create_temp('51819846.jpg')
decrypt_file(name)
