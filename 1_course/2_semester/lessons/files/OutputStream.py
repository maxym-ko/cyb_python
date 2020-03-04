class FlaotInputStream:
    _len = 1024

    def __init__(self, path):
        self._f = open(path)
        self._buf = ''
        self._cur = 0
        self._parts = []
        self._eof = False

    def read(self):
        pass

    def _read_next_partion(self):
        self._buf = self._f.readline(self._len)
        self._cur = 0
        self._eof = not self._buf
        return self._eof
