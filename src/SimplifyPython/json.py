class sjson:
    def open(filepath='data.json'):
        import json
        global the_file
        the_file = filepath
        with open(filepath) as f:
            data = json.load(f)
        return data

    def save(data={}, filepath='the_file', formatted=True):
        import json
        from os.path import exists
        if filepath == 'the_file':
            filepath == the_file
        if exists(filepath):
            with open(filepath, 'w') as f:
                if formatted is True:
                    json.dump(data, f, indent=4)
                else:
                    json.dump(data, f)
            return True
        elif exists(the_file):
            with open(the_file, 'w') as f:
                if formatted is True:
                    json.dump(data, f, indent=4)
                else:
                    json.dump(data, f)
            return True
        else:
            from .colors import colors
            print(f'{colors.FAIL}No files found try creating one with sjson.new()')

    def new(filename='data.json'):
        from os.path import exists
        presplit = filename.split(".")
        if len(presplit) == 1:
            filename += ".json"
        else:
            filename = presplit
        if not exists(filename):
            split = filename.split(".")
            if len(split) == 1:
                f = open(f"{filename}.json", "w")
                f.write("{}")
                f.close()
                return True
            elif len(split) < 1:
                from .colors import colors
                print(f'{colors.FAIL}Filename must not be blank.')
                return False
            else:
                f = open(filename, "w")
                f.write("{}")
                f.close()
                return True
        else:
            return 'File already exists'
