import json
from errors import *


class Builder:
    @staticmethod
    def load(student, filename_csv, filename_json, encoding):
        Builder.load_data(student, filename_csv, encoding)
        print("OK")
        lst_stat = Builder.load_stat(filename_json, encoding)
        print("OK")
        return Builder.fit(student, lst_stat)

    @staticmethod
    def load_data(student, filename, encoding):
        print("input-csv " + filename + ": ", end="")
        pass

    # Todo: ask about keys in json file (excellent and mark ???), ask if I can output from this method
    @staticmethod
    def load_stat(filename, encoding):
        print("input-json " + filename + ": ", end="")
        try:
            with open(filename, encoding=encoding) as f:
                stat_dict = json.load(f)
        except OSError:
            raise OpenJsonError("Cannot read json file")
        stat_keys = ["кількість «відмінно»", "сума державних оцінок"]
        if not all(k in stat_dict for k in stat_keys):
            raise ReadJsonError("There are no required keys in the .json file")
        stat_dict["excellent"] = stat_dict.pop("кількість «відмінно»")
        stat_dict["mark"] = stat_dict.pop("сума державних оцінок")
        return stat_dict



    @staticmethod
    def fit(student, lst_stat):
        print("json?=csv: ", end="")
        # do smth
        return NotImplemented
