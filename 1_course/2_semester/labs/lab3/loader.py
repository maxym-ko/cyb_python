"""
Author: Maxym Koval (Group K-12)
"""

import json

from builder import Builder
from errors import ReadJsonError, LoadJsonError


def load(information, filename_csv, filename_json, encoding):
    print("input-csv " + filename_csv + ": ", end="")
    load_data(information, filename_csv, encoding)
    print("OK")
    print("input-json " + filename_json + ": ", end="")
    stat_dict = load_stat(filename_json, encoding)
    print("OK")
    print("json?=csv: ", end="")
    fit(information, stat_dict)
    print("OK")
    return True


def load_data(information, filename, encoding):
    Builder(information, filename, encoding).load()


def load_stat(filename, encoding):
    try:
        with open(filename, encoding=encoding) as f:
            stat_dict = json.load(f)
    except OSError:
        raise ReadJsonError("Cannot read(open) .json file")
    stat_keys = ["кількість «відмінно»", "сума державних оцінок"]
    if not all(k in stat_dict for k in stat_keys):
        raise LoadJsonError("There are no required keys in the .json file")
    stat_dict["excellent_count"] = stat_dict.pop("кількість «відмінно»")
    stat_dict["mark_sum"] = stat_dict.pop("сума державних оцінок")
    return stat_dict


def fit(information, stat_dict):
    if stat_dict["excellent_count"] != information.excellent_count and stat_dict["mark_sum"] != information.mark_sum:
        raise IndentationError
    return True
