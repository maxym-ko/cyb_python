import json
import csv
from errors import *


class Builder:
    def __init__(self, information, filename_csv, filename_json, encoding):
        self._information = information
        self._filename_csv = filename_csv
        self._filename_json = filename_json
        self._encoding = encoding
        self._loaded = False
        self._line = ""
        self._stat_dict = []
        self._transcript_id = ""
        self._group_id = ""
        self._name = ""
        self._surname = ""
        self._patronymic = ""
        self._subject_name = ""
        self._total_points = 0
        self._mark = 0
        self._exam_points = 0

    def load(self):
        if self._loaded:
            return False
        print("input-csv " + self.filename_csv + ": ", end="")
        self.load_data()
        print("OK")
        print("input-json " + self.filename_json + ": ", end="")
        self._stat_dict = self.load_stat()
        print("OK")
        return self.fit()

    # Todo: what to do with first line
    def load_data(self):
        try:
            with self.information, open(self.filename_csv) as file:
                it = csv.reader(file, delimiter=';')
                next(it)
                for self._line in it:
                    if self._line:
                        self._process_current_line()
                        self.information.load(self._transcript_id, self._group_id, self._name, self._surname, self._patronymic, self._subject_name, self._total_points, self._mark, self._exam_points)
        except OSError:
            raise OpenCsvError("Cannot read(open) .csv file")

    def _process_current_line(self):
        if len(self._line) != 9:
            # Todo: what to do here?
            pass
        else:
            self._transcript_id = self._line[0]
            self._mark = self._line[1]
            self._subject_name = self._line[2]
            self._patronymic = self._line[3]
            self._exam_points = self._line[4]
            self._surname = self._line[5]
            self._name = self._line[6]
            self._total_points = self._line[7]
            self._group_id = self._line[8]
            self._covert_variables()

    def _covert_variables(self):
        try:
            self._total_points = int(self._total_points)
            self._mark = int(self._mark)
            self._exam_points = int(self._exam_points)
        except ValueError:
            raise ReadCsvError("Some of the fields can't be converted")

    # Todo: ask if I can output from this method
    def load_stat(self):
        try:
            with open(self.filename_json, encoding=self.encoding) as f:
                self._stat_dict = json.load(f)
        except OSError:
            raise OpenJsonError("Cannot read(open) .json file")
        stat_keys = ["кількість «відмінно»", "сума державних оцінок"]
        if not all(k in self._stat_dict for k in stat_keys):
            raise ReadJsonError("There are no required keys in the .json file")
        self._stat_dict["excellent"] = self._stat_dict.pop("кількість «відмінно»")
        self._stat_dict["mark"] = self._stat_dict.pop("сума державних оцінок")
        return self._stat_dict

    def fit(self):
        print("json?=csv: ", end="")
        try:
            pass
        except:
            pass
        return NotImplemented

    @property
    def information(self):
        return self._information

    @property
    def filename_csv(self):
        return self._filename_csv

    @property
    def filename_json(self):
        return self._filename_json

    @property
    def encoding(self):
        return self._encoding
