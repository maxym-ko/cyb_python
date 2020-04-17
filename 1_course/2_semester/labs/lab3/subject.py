class Subject:
    def __init__(self, subject_name):
        self._subject_name = subject_name
        self._total_points = 0
        self._mark = 0
        self._exam_points = 0
        self._passed = False

    def load(self, total_points: int, mark: int, exam_points: int) -> bool:
        self._total_points = total_points
        self._mark = mark
        self._exam_points = exam_points
        self._passed = self.mark > 2
        return self.passed

    def __eq__(self, other):
        return self.subject_name == other.subject_name

    @property
    def subject_name(self):
        return self._subject_name

    @property
    def total_points(self):
        return self._total_points

    @property
    def mark(self):
        return self._mark

    @property
    def exam_points(self):
        return self._exam_points

    @property
    def passed(self):
        return self._passed
