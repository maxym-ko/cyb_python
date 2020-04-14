class Student:
    def clear(self):
        pass

    def output(self, filename, encoding):
        print("output " + filename + ": ", end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.clear()

    def __enter__(self):
        self.clear()
