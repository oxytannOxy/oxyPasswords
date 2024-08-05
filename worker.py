import json
from random import randint


class Worker:

    def __init__(self):
        self.generated_pass: str

    def password_gen(self):
        with open("data/settings.json", "r") as data:
            d = json.load(data)
            sig = d["settings"]["signature"]
            sym = d["settings"]["symbols"]
            num = d["settings"]["numbers"]

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        n1 = [numbers[randint(0, len(numbers)-1)] for f in range(int(num))]
        s2 = [symbols[randint(0, len(symbols)-1)] for g in range(int(sym))]

        n = "".join(n1)
        s = "".join(s2)
        sig = sig
        password = sig+n+s
        return password

    def save_settings(self, set_dict:dict):
        try:
            with open("data/settings.json", "r") as data:
                json_data = json.load(data)
                json_data.update(set_dict)
            with open("data/settings.json", "w") as data:
                json.dump(json_data, data, indent=4)

        except:
            with open("data/settings.json", "w") as data:
                json.dump(set_dict, data, indent=4)

    def save_password(self, pass_dict: dict,):
        try:
            with open("data/passwords.json", "r") as data:
                json_data = json.load(data)
                json_data.update(pass_dict)
            with open("data/passwords.json", "w") as data:
                json.dump(json_data, data, indent=4)

        except Exception:
            with open("data/passwords.json", "w") as data:
                json.dump(pass_dict, data, indent=4)

    def read_passwords_for_scrollbar(self):
        with open("data/passwords.json", "r") as data:
            pass_json = json.load(data)
            number_of_passwords = len(pass_json)

        try:
            pass_tup = []
            for key in pass_json:
                pass_tup.append((key, pass_json[key]["gmail"], pass_json[key]["password"]))

            return pass_tup

        except Exception:
            return []

    def delete(self, key: str):
        will_delete = key

        with open("data/passwords.json", "r") as data:
            json_data = json.load(data)
            del json_data[will_delete]

        with open("data/passwords.json", "w") as data:
            json.dump(json_data, data, indent=4)
