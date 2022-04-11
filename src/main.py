from time import time

from SimplifyPython import sflask

var = 10
sflask.create_page("/", "hello, world!")
sflask.create_page("/no", "goodbye")
sflask.launch_pages().start()
