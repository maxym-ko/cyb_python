import json
from errors import *


class Builder:
    @staticmethod
    def load(information, filename_csv, filename_json, encoding):
        print("input-csv " + filename_csv + ": ", end="")
        Builder.load_data(information, filename_csv, encoding)
        print("OK")
        print("input-json " + filename_json + ": ", end="")
        lst_stat = Builder.load_stat(filename_json, encoding)
        print("OK")
        return Builder.fit(information, lst_stat)

    @staticmethod
    def load_data(information, filename, encoding):
        try:
            with information as information:
                pass
        except OSError:
            raise OpenCsvError("Cannot read(open) .csv file")

    # Todo: ask if I can output from this method, ask about @staticmethod (is it good?)
    @staticmethod
    def load_stat(filename, encoding):
        try:
            with open(filename, encoding=encoding) as f:
                stat_dict = json.load(f)
        except OSError:
            raise OpenJsonError("Cannot read(open) .json file")
        stat_keys = ["кількість «відмінно»", "сума державних оцінок"]
        if not all(k in stat_dict for k in stat_keys):
            raise ReadJsonError("There are no required keys in the .json file")
        stat_dict["excellent"] = stat_dict.pop("кількість «відмінно»")
        stat_dict["mark"] = stat_dict.pop("сума державних оцінок")
        return stat_dict

    @staticmethod
    def fit(information, lst_stat):
        print("json?=csv: ", end="")
        try:
            pass
        except:
            pass
        return NotImplemented
