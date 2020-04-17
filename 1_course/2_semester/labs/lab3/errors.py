class Error(BaseException):
    def __init__(self, exception):
        self._exc = exception

    def __repr__(self):
        return ''


class CommandLineError(Error):
    def __repr__(self):
        return "***** command line error error *****"


class InitError(Error):
    def __repr__(self):
        return "***** init file error *****"


class ReadCsvError(Error):
    def __repr__(self):
        return "***** can not read input csv-file *****"


class LoadCsvError(Error):
    def __repr__(self):
        return "***** incorrect input csv-file *****"


class ReadJsonError(Error):
    def __repr__(self):
        return "***** can not read input json-file *****"


class LoadJsonError(Error):
    def __repr__(self):
        return "***** incorrect input json-file *****"


class ConsistentError(Error):
    def __repr__(self):
        return "***** inconsistent information *****"


class OutputError(Error):
    def __repr__(self):
        return "***** can not write output file *****"
