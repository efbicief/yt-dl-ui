import locale
import json

class Locale():

    def __init__(self):

        locale_name = locale.getdefaultlocale()[0]

        json_path = "locale/locale_" + locale_name + ".json"
        try:
            json_data = open(json_path, 'r')

        except FileNotFoundError:
            print('[WARNING] Locale file "' + json_path + '" not found.')
            lcshort = str(locale_name.split('_')[0])
            json_path = "locale/locale_" + lcshort + ".json"

            try:
                json_data = open(json_path, 'r')
                print('Locale "' + json_path + '" successfully imported.')

            except FileNotFoundError:
                print('[WARNING] Locale file "' + json_path + '" not found. Defaulting to "locale/locale_en.json".')
                json_data = open("locale/locale_en.json", 'r')
                print('Locale "locale/locale_en.json" successfully imported.')

        self.lang = json.loads(json_data.read())

        json_data.close()