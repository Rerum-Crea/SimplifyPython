class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def create_page(route="/", horm=":)"):
    global htmlpagenum
    global pagenum
    try:
        if not done:
            initialize(True)
        htmlpagenum = initialize(True)
        pagenum = initialize(False)
        if ".html" in horm:
            if htmlpagenum <= 50:
                route_message_html[htmlpagenum]["route"] = route
                route_message_html[htmlpagenum]["html-path"] = horm
                htmlpagenum += 1
            else:
                print(f"{bcolors.WARNING}No HTML Pages Left to use :(")
        else:
            if pagenum <= 50:
                route_message[pagenum]["route"] = route
                route_message[pagenum]["message"] = horm
                pagenum += 1
            else:
                print(f"{bcolors.WARNING}No Pages Left to use :(")
    except NameError:
        initialize(True)
        htmlpagenum = initialize(True)
        pagenum = initialize(False)
        if ".html" in horm:
            if htmlpagenum <= 50:
                route_message_html[htmlpagenum]["route"] = route
                route_message_html[htmlpagenum]["html-path"] = horm
                htmlpagenum += 1
            else:
                print(f"{bcolors.WARNING}No HTML Pages Left to use :(")
        else:
            if pagenum <= 50:
                route_message[pagenum]["route"] = route
                route_message[pagenum]["message"] = horm
                pagenum += 1
            else:
                print(f"{bcolors.WARNING}No Pages Left to use :(")


def launch_pages(port=6969, daemon=False):
    from threading import Thread

    thread_data = Thread(
        target=launch_pages_internals,
        args=(port, route_message_html, route_message, pagenum, htmlpagenum),
        daemon=daemon,
    )
    return thread_data


def launch_pages_nothread(port=6969):
    launch_pages_internals(port, route_message_html, route_message, pagenum,
                           htmlpagenum)


def initialize(html):
    global route_message_html
    global route_message
    global pagenum
    global htmlpagenum
    global done
    try:
        done + 1
    except NameError:
        pagenum = 0
        htmlpagenum = 0
        route_message_html = {}
        route_message = {}
        for i in range(50):
            route_message_html[i] = {}
            route_message[i] = {}
            route_message_html[i][
                "route"] = "/PingServerIsTheBestForThingsLikeLongURLSJK"
            route_message[i][
                "route"] = "/PingServerIsTheBestForThingsLikeLongURLSJK"
            route_message_html[i]["message"] = ":("
            route_message[i][
                "html-path"] = "If you use the default for html your bad"
        done = True
    if done is True:
        if html is True:
            return htmlpagenum
        else:
            return pagenum


def launch_pages_internals(port, route_message_html, route_message, pageamt,
                           htmlpageamt):
    import random

    from flask import Flask

    if port == 6969:
        port = random.randint(2000, 9000)

    app = Flask("app")
    print(htmlpageamt, "&", pageamt)
    # 1
    if htmlpageamt <= 1:
        html_1(app, route_message_html)
    if pageamt <= 1:
        string_1(app, route_message)

    # 10
    if htmlpageamt > 1:
        if htmlpageamt <= 10:
            html_1(app, route_message_html)
            html_10(app, route_message_html)
    if pageamt > 1:
        if pageamt <= 10:
            string_1(app, route_message)
            string_10(app, route_message)

    # 20
    if htmlpageamt > 10:
        if htmlpageamt <= 20:
            html_1(app, route_message_html)
            html_10(app, route_message_html)
            html_20(app, route_message_html)
    if pageamt > 10:
        if pageamt <= 20:
            string_1(app, route_message)
            string_10(app, route_message)
            string_20(app, route_message)

    # 30
    if htmlpageamt > 20:
        if htmlpageamt <= 30:
            html_1(app, route_message_html)
            html_10(app, route_message_html)
            html_20(app, route_message_html)
            html_30(app, route_message_html)
    if pageamt > 20:
        if pageamt <= 30:
            string_1(app, route_message)
            string_10(app, route_message)
            string_20(app, route_message)
            string_30(app, route_message)

    # 40
    if htmlpageamt > 30:
        if htmlpageamt <= 40:
            html_1(app, route_message_html)
            html_10(app, route_message_html)
            html_20(app, route_message_html)
            html_30(app, route_message_html)
            html_40(app, route_message_html)
    if pageamt > 30:
        if pageamt <= 40:
            string_1(app, route_message)
            string_10(app, route_message)
            string_20(app, route_message)
            string_30(app, route_message)
            string_40(app, route_message)

    # 50
    if htmlpageamt > 40:
        if htmlpageamt <= 50:
            html_1(app, route_message_html)
            html_10(app, route_message_html)
            html_20(app, route_message_html)
            html_30(app, route_message_html)
            html_40(app, route_message_html)
            html_50(app, route_message_html)
    if pageamt > 40:
        if pageamt <= 50:
            string_1(app, route_message)
            string_10(app, route_message)
            string_20(app, route_message)
            string_30(app, route_message)
            string_40(app, route_message)
            string_50(app, route_message)

    # >50
    if htmlpageamt >= 51:
        html_10(app, route_message_html)
        html_20(app, route_message_html)
        html_30(app, route_message_html)
        html_40(app, route_message_html)
        html_50(app, route_message_html)
    if pageamt >= 51:
        string_1(app, route_message)
        string_10(app, route_message)
        string_20(app, route_message)
        string_30(app, route_message)
        string_40(app, route_message)
        string_50(app, route_message)

    app.run(host="0.0.0.0", port=port)


def string_1(app, route_message):

    @app.route(route_message[0]["route"])
    def Server_0():
        return route_message[0]["message"]


def string_10(app, route_message):

    @app.route(route_message[1]["route"])
    def Server_1():
        return route_message[1]["message"]

    @app.route(route_message[2]["route"])
    def Server_2():
        return route_message[2]["message"]

    @app.route(route_message[3]["route"])
    def Server_3():
        return route_message[3]["message"]

    @app.route(route_message[4]["route"])
    def Server_4():
        return route_message[4]["message"]

    @app.route(route_message[5]["route"])
    def Server_5():
        return route_message[5]["message"]

    @app.route(route_message[6]["route"])
    def Server_6():
        return route_message[6]["message"]

    @app.route(route_message[7]["route"])
    def Server_7():
        return route_message[7]["message"]

    @app.route(route_message[8]["route"])
    def Server_8():
        return route_message[8]["message"]

    @app.route(route_message[9]["route"])
    def Server_9():
        return route_message[9]["message"]


def string_20(app, route_message):

    @app.route(route_message[10]["route"])
    def Server_10():
        return route_message[10]["message"]

    @app.route(route_message[11]["route"])
    def Server_11():
        return route_message[11]["message"]

    @app.route(route_message[12]["route"])
    def Server_12():
        return route_message[12]["message"]

    @app.route(route_message[13]["route"])
    def Server_13():
        return route_message[13]["message"]

    @app.route(route_message[14]["route"])
    def Server_14():
        return route_message[14]["message"]

    @app.route(route_message[15]["route"])
    def Server_15():
        return route_message[15]["message"]

    @app.route(route_message[16]["route"])
    def Server_16():
        return route_message[16]["message"]

    @app.route(route_message[17]["route"])
    def Server_17():
        return route_message[17]["message"]

    @app.route(route_message[18]["route"])
    def Server_18():
        return route_message[18]["message"]

    @app.route(route_message[19]["route"])
    def Server_19():
        return route_message[19]["message"]


def string_30(app, route_message):

    @app.route(route_message[20]["route"])
    def Server_20():
        return route_message[20]["message"]

    @app.route(route_message[21]["route"])
    def Server_21():
        return route_message[21]["message"]

    @app.route(route_message[22]["route"])
    def Server_22():
        return route_message[22]["message"]

    @app.route(route_message[23]["route"])
    def Server_23():
        return route_message[23]["message"]

    @app.route(route_message[24]["route"])
    def Server_24():
        return route_message[24]["message"]

    @app.route(route_message[25]["route"])
    def Server_25():
        return route_message[25]["message"]

    @app.route(route_message[26]["route"])
    def Server_26():
        return route_message[26]["message"]

    @app.route(route_message[27]["route"])
    def Server_27():
        return route_message[27]["message"]

    @app.route(route_message[28]["route"])
    def Server_28():
        return route_message[28]["message"]

    @app.route(route_message[29]["route"])
    def Server_29():
        return route_message[29]["message"]


def string_40(app, route_message):

    @app.route(route_message[30]["route"])
    def Server_30():
        return route_message[30]["message"]

    @app.route(route_message[31]["route"])
    def Server_31():
        return route_message[31]["message"]

    @app.route(route_message[32]["route"])
    def Server_32():
        return route_message[32]["message"]

    @app.route(route_message[33]["route"])
    def Server_33():
        return route_message[33]["message"]

    @app.route(route_message[34]["route"])
    def Server_34():
        return route_message[34]["message"]

    @app.route(route_message[35]["route"])
    def Server_35():
        return route_message[35]["message"]

    @app.route(route_message[36]["route"])
    def Server_36():
        return route_message[36]["message"]

    @app.route(route_message[37]["route"])
    def Server_37():
        return route_message[37]["message"]

    @app.route(route_message[38]["route"])
    def Server_38():
        return route_message[38]["message"]

    @app.route(route_message[39]["route"])
    def Server_39():
        return route_message[39]["message"]


def string_50(app, route_message):

    @app.route(route_message[40]["route"])
    def Server_40():
        return route_message[40]["message"]

    @app.route(route_message[41]["route"])
    def Server_41():
        return route_message[41]["message"]

    @app.route(route_message[42]["route"])
    def Server_42():
        return route_message[42]["message"]

    @app.route(route_message[43]["route"])
    def Server_43():
        return route_message[43]["message"]

    @app.route(route_message[44]["route"])
    def Server_44():
        return route_message[44]["message"]

    @app.route(route_message[45]["route"])
    def Server_45():
        return route_message[45]["message"]

    @app.route(route_message[46]["route"])
    def Server_46():
        return route_message[46]["message"]

    @app.route(route_message[47]["route"])
    def Server_47():
        return route_message[47]["message"]

    @app.route(route_message[48]["route"])
    def Server_48():
        return route_message[48]["message"]

    @app.route(route_message[49]["route"])
    def Server_49():
        return route_message[49]["message"]


def html_1(app, route_message_html):
    from flask import render_template

    @app.route(route_message_html[0]["route"])
    def Server_50():
        return render_template(route_message_html[0]["html-path"])


def html_10(app, route_message_html):
    from flask import render_template

    @app.route(route_message_html[1]["route"])
    def Server_51():
        return render_template(route_message_html[1]["html-path"])

    @app.route(route_message_html[2]["route"])
    def Server_52():
        return render_template(route_message_html[2]["html-path"])

    @app.route(route_message_html[3]["route"])
    def Server_53():
        return render_template(route_message_html[3]["html-path"])

    @app.route(route_message_html[4]["route"])
    def Server_54():
        return render_template(route_message_html[4]["html-path"])

    @app.route(route_message_html[5]["route"])
    def Server_55():
        return render_template(route_message_html[5]["html-path"])

    @app.route(route_message_html[6]["route"])
    def Server_56():
        return render_template(route_message_html[6]["html-path"])

    @app.route(route_message_html[7]["route"])
    def Server_57():
        return render_template(route_message_html[7]["html-path"])

    @app.route(route_message_html[8]["route"])
    def Server_58():
        return render_template(route_message_html[8]["html-path"])

    @app.route(route_message_html[9]["route"])
    def Server_59():
        return render_template(route_message_html[9]["html-path"])


def html_20(app, route_message_html):
    from flask import render_template

    @app.route(route_message_html[10]["route"])
    def Server_60():
        return render_template(route_message_html[10]["html-path"])

    @app.route(route_message_html[11]["route"])
    def Server_61():
        return render_template(route_message_html[11]["html-path"])

    @app.route(route_message_html[12]["route"])
    def Server_62():
        return render_template(route_message_html[12]["html-path"])

    @app.route(route_message_html[13]["route"])
    def Server_63():
        return render_template(route_message_html[13]["html-path"])

    @app.route(route_message_html[14]["route"])
    def Server_64():
        return render_template(route_message_html[14]["html-path"])

    @app.route(route_message_html[15]["route"])
    def Server_65():
        return render_template(route_message_html[15]["html-path"])

    @app.route(route_message_html[16]["route"])
    def Server_66():
        return render_template(route_message_html[16]["html-path"])

    @app.route(route_message_html[17]["route"])
    def Server_67():
        return render_template(route_message_html[17]["html-path"])

    @app.route(route_message_html[18]["route"])
    def Server_68():
        return render_template(route_message_html[18]["html-path"])

    @app.route(route_message_html[19]["route"])
    def Server_69():
        return render_template(route_message_html[19]["html-path"])


def html_30(app, route_message_html):
    from flask import render_template

    @app.route(route_message_html[20]["route"])
    def Server_70():
        return render_template(route_message_html[20]["html-path"])

    @app.route(route_message_html[21]["route"])
    def Server_71():
        return render_template(route_message_html[21]["html-path"])

    @app.route(route_message_html[22]["route"])
    def Server_72():
        return render_template(route_message_html[22]["html-path"])

    @app.route(route_message_html[23]["route"])
    def Server_73():
        return render_template(route_message_html[23]["html-path"])

    @app.route(route_message_html[24]["route"])
    def Server_74():
        return render_template(route_message_html[24]["html-path"])

    @app.route(route_message_html[25]["route"])
    def Server_75():
        return render_template(route_message_html[25]["html-path"])

    @app.route(route_message_html[26]["route"])
    def Server_76():
        return render_template(route_message_html[26]["html-path"])

    @app.route(route_message_html[27]["route"])
    def Server_77():
        return render_template(route_message_html[27]["html-path"])

    @app.route(route_message_html[28]["route"])
    def Server_78():
        return render_template(route_message_html[28]["html-path"])

    @app.route(route_message_html[29]["route"])
    def Server_79():
        return render_template(route_message_html[29]["html-path"])


def html_40(app, route_message_html):
    from flask import render_template

    @app.route(route_message_html[30]["route"])
    def Server_80():
        return render_template(route_message_html[30]["html-path"])

    @app.route(route_message_html[31]["route"])
    def Server_81():
        return render_template(route_message_html[31]["html-path"])

    @app.route(route_message_html[32]["route"])
    def Server_82():
        return render_template(route_message_html[32]["html-path"])

    @app.route(route_message_html[33]["route"])
    def Server_83():
        return render_template(route_message_html[33]["html-path"])

    @app.route(route_message_html[34]["route"])
    def Server_84():
        return render_template(route_message_html[34]["html-path"])

    @app.route(route_message_html[35]["route"])
    def Server_85():
        return render_template(route_message_html[35]["html-path"])

    @app.route(route_message_html[36]["route"])
    def Server_86():
        return render_template(route_message_html[36]["html-path"])

    @app.route(route_message_html[37]["route"])
    def Server_87():
        return render_template(route_message_html[37]["html-path"])

    @app.route(route_message_html[38]["route"])
    def Server_88():
        return render_template(route_message_html[38]["html-path"])

    @app.route(route_message_html[39]["route"])
    def Server_89():
        return render_template(route_message_html[39]["html-path"])


def html_50(app, route_message_html):
    from flask import render_template

    @app.route(route_message_html[40]["route"])
    def Server_90():
        return render_template(route_message_html[40]["html-path"])

    @app.route(route_message_html[41]["route"])
    def Server_91():
        return render_template(route_message_html[41]["html-path"])

    @app.route(route_message_html[42]["route"])
    def Server_92():
        return render_template(route_message_html[42]["html-path"])

    @app.route(route_message_html[43]["route"])
    def Server_93():
        return render_template(route_message_html[43]["html-path"])

    @app.route(route_message_html[44]["route"])
    def Server_94():
        return render_template(route_message_html[44]["html-path"])

    @app.route(route_message_html[45]["route"])
    def Server_95():
        return render_template(route_message_html[45]["html-path"])

    @app.route(route_message_html[46]["route"])
    def Server_96():
        return render_template(route_message_html[46]["html-path"])

    @app.route(route_message_html[47]["route"])
    def Server_97():
        return render_template(route_message_html[47]["html-path"])

    @app.route(route_message_html[48]["route"])
    def Server_98():
        return render_template(route_message_html[48]["html-path"])

    @app.route(route_message_html[49]["route"])
    def Server_99():
        return render_template(route_message_html[49]["html-path"])
