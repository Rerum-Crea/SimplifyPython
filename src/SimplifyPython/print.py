class sprint:
    global RED
    global PINK
    global PURPLE
    global BLUE
    global LIGHTBLUE
    global BRIGHTBLUE
    global GREEN
    global LIGHTGREEN
    global YELLOW
    global ORANGE
    global WHITE
    RED = "\033[38:5:196m"
    PINK = "\033[38:5:163m"
    PURPLE = "\033[38:5:92m"
    BLUE = "\033[38:5:20m"
    LIGHTBLUE = "\033[38:5:27m"
    BRIGHTBLUE = "\033[38:5:33m"
    GREEN = "\033[38:5:40m"
    LIGHTGREEN = "\033[38:5:82m"
    YELLOW = "\033[38:5:11m"
    ORANGE = "\033[38:5:202m"
    WHITE = "\033[38:5:15m"

    def process(message):
        cmessage = ""
        for i in range(len(message)):
            cmessage += message[i]
            cmessage += " "
        return cmessage

    def red(*message):
        print(f"{RED}{sprint.process(message)}{WHITE}")

    def pink(*message):
        print(f"{PINK}{sprint.process(message)}{WHITE}")

    def purple(*message):
        print(f"{PURPLE}{sprint.process(message)}{WHITE}")

    def blue(*message):
        print(f"{BLUE}{sprint.process(message)}{WHITE}")

    def lightblue(*message):
        print(f"{LIGHTBLUE}{sprint.process(message)}{WHITE}")

    def brightblue(*message):
        print(f"{BRIGHTBLUE}{sprint.process(message)}{WHITE}")

    def green(*message):
        print(f"{GREEN}{sprint.process(message)}{WHITE}")

    def lightgreen(*message):
        print(f"{LIGHTGREEN}{sprint.process(message)}{WHITE}")

    def yellow(*message):
        print(f"{YELLOW}{sprint.process(message)}{WHITE}")

    def orange(*message):
        print(f"{ORANGE}{sprint.process(message)}{WHITE}")
