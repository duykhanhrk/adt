import data_center
import storage
import support
import tutorial
import message

default_options = {
    'method': '--o'
}

def act(db, url, options):
    ext_json = storage.load_ext(options["ext"])

    if options["method"] == "--a":
        data = []
        page = 0

        while True:
            page += 1
            page_url = support.map_vari(ext_json["page"], [ {"var": "$link", "value": url}, {"var": "$page", "value": page}])
            
            html_text = ""
            try:
                html_text = support.get_data_from_url(page_url)
            except:
                message.error_message(page_url, "cng")
                return False
            
            data_extracted = []
            try:
                data_extracted = tutorial.handle(ext_json, html_text)
            except:
                message.error_message(options["ext"], "epd")
                return False

            if len(data_extracted) == 0:
                break

            data = data + data_extracted
            message.progress_message("s", "GET {}".format(page_url))

        data_center.append_database(db, data)
    elif options["method"] == "--o":
        html_text = ""
        try:
            html_text = support.get_data_from_url(url)
        except:
            message.error_message(url, "cng")
            return False
            
        try:
            data = tutorial.handle(ext_json, html_text)
        except:
            message.error_message(options["ext"], "epd")
            return False

        message.progress_message("s", "GET {}".format(url))

        data_center.append_database(db, data)
    elif options["method"] == "-f":
        data = []

        for page in range(options["from_page"], options["to_page"] + 1):
            page_url = support.map_vari(ext_json["page"], [ {"var": "$link", "value": url}, {"var": "$page", "value": page}])
            
            html_text = ""
            try:
                html_text = support.get_data_from_url(page_url)
            except:
                message.error_message(page_url, "cng")
                return False
            
            data_extracted = []
            try:
                data_extracted = tutorial.handle(ext_json, html_text)
            except:
                message.error_message(options["ext"], "epd")
                return False

            if len(data_extracted) == 0:
                break

            data = data + data_extracted
            message.progress_message("s", "GET {}".format(page_url))

        data_center.append_database(db, data)
    elif options["method"] == "-s":
        data = []

        for page in options["pages"]:
            page_url = support.map_vari(ext_json["page"], [ {"var": "$link", "value": url}, {"var": "$page", "value": page}])
            
            html_text = ""
            try:
                html_text = support.get_data_from_url(page_url)
            except:
                message.error_message(page_url, "cng")
                return False
            
            data_extracted = []
            try:
                data_extracted = tutorial.handle(ext_json, html_text)
            except:
                message.error_message(options["ext"], "epd")
                return False

            if len(data_extracted) == 0:
                break

            data = data + data_extracted
            message.progress_message("s", "GET {}".format(page_url))

        data_center.append_database(db, data)

    return True

def handle(command):
    options = default_options

    if "-e" in command:
        loc = command.index("-e")
        if loc + 2 > 0:
            message.error_message("EXT ID:NULL", "cmw")
            return False

        if not storage.does_ext_exist(command[loc + 1]):
            message.error_message(command[loc + 1], "etn")
            return False

        options["ext"] = command[loc + 1]

        command.pop(loc)
        command.pop(loc)

    if "--a" in command:
        options["method"] = "--a"
        command.remove("--a")
    elif "--o" in command:
        options["method"] = "--o"
        command.remove("--o")
    elif "-f" in command:
        options["method"] = "-f"
        loc = command.index("-f")

        if loc + 2 > len(command):
            message.error_message("FROM PAGE:NULL", "cmw")
            return False

        if loc + 3 > len(command):
            message.error_message("TO PAGE:NULL", "cmw")
            return False

        from_page = support.to_int(command[loc + 1])
        if from_page == None or from_page < 1:
            message.error_message("FROM PAGE:{}".format(from_page), "mpi")
            return False

        to_page = support.to_int(command[loc + 2])
        if to_page == None or to_page < 1:
            message.error_message("FROM PAGE:{}".format(to_page), "mpi")
            return False

        if from_page > to_page:
            from_page, to_page = to_page, from_page

        options['from_page'] = from_page
        options['to_page'] = to_page

        command.pop(loc)
        command.pop(loc)
        command.pop(loc)
    elif "-s" in command:
        options["method"] = "-s"
        loc = command.index("-s")

        if loc + 2 > len(command):
            message.error_message("PAGE:NULL", "cmw")
            return False

        pages = []
        for i in range(loc + 1, len(command)):
            page = support.to_int(command[i])
            if page == None or page < 1:
                message.error_message("PAGE:{}".format(page), "mpi")
                return False
            pages.append(page)

        options["pages"] = pages
        
        command = command[:loc]

    if len(command) == 0:
        message.error_message("DB:NULL", "cmw")
        return False

    if len(command) == 1:
        message.error_message("URL:NULL", "cmw")
        return False

    if len(command) == 2:
        if data_center.in_databases(command[0]):
            message.error_message(command[0], "dbe")
            return False

        if not "ext" in options:
            options['ext'] = support.choose_ext(command[1])

            if options['ext'] == None:
                message.error_message(command[1], 'sns')
                return False
        else:
            if support.does_ext_support_server(options['ext'], command[1]):
                message.error_message(command[1], 'sns')
                return False

        return act(command[0], command[1], options)
    

    message.error_message(command[2], "cmd")
    return False
    