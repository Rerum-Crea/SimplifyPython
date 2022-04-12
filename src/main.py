from fileinput import filename
import requests
import easygui
from SimplifyPython import sfile

def main():
    filepath = easygui.fileopenbox()
    # sfile.send_encrypted('https://Messin.necrownyx.repl.co', filepath, b'qUVKJy_nN8H8TUSkhbC2X7WjfX7jm51BhD_KbjUwkZw=')
    sfile.send('https://Messin.necrownyx.repl.co', filepath)

main()