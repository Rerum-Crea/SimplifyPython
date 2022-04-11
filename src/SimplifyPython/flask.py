class sflask:
    from .flask_internals import bcolors, create_page, launch_pages, launch_pages_nothread


    def start(route="/", horm=':)', port=6969):
        from .flask_internals import bcolors, create_page, launch_pages, launch_pages_nothread
        import random
        if port == 6969:
            port = random.randint(2000, 9000)
        create_page(route, horm)
        launch_pages_nothread(port)


    def thread(message=":)", route='/', port=6969, daemon=False):
        from .flask_internals import bcolors, create_page, launch_pages, launch_pages_nothread
        from threading import Thread
        thread_data = Thread(target=sflask.start, args=(route, message, port), daemon=daemon)
        return thread_data


    class help:
        def __init__(self):
            from .print import sprint
            sprint.BRIGHTBLUE("###########################################################")
            sprint.BRIGHTBLUE("To get info on the different modules please goto:")
            sprint.BRIGHTBLUE("https://github.com/Necrownyx/PingServer/blob/main/README.md")
            sprint.BRIGHTBLUE("###########################################################")