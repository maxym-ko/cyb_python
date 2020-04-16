from student import Student
from errors import ReadCsvError


class Information:
    def __init__(self):
        self._students = []
        self._mark_sum = 0
        self._excellent_count = 0

    def load(self, transcript_id: str, group_id: str, name: str, surname: str, patronymic: str, subject_name: str, total_points: int, mark: int, exam_points: int):
        if (student := self._find(transcript_id)) is None:
            student = self._add(transcript_id, group_id, name, surname, patronymic)
        if not (student.group_id == group_id and student.name == name and student.surname == surname and student.patronymic == patronymic):
            raise ReadCsvError("Inconsistent information in .csv file")
        student.load(subject_name, total_points, mark, exam_points)

    # Todo ask about "Student(transcript_id)"
    def _find(self, transcript_id: str) -> Student:
        st_index = self._students.index(Student(transcript_id, "", "", "", ""))
        return None if st_index == -1 else self._students[st_index]

    def _add(self, transcript_id: str, group_id: str, name: str, surname: str, patronymic: str) -> Student:
        self._students.append(Student(transcript_id, group_id, name, surname, patronymic))
        return self._students[-1]

    def output(self, filename, encoding):
        print("output " + filename + ": ", end="")

    def clear(self):
        self._students.clear()
        self._mark_sum = 0
        self._excellent_count = 0

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.clear()

    def __enter__(self):
        self.clear()

    @property
    def mark_sum(self):
        return self._mark_sum

    @property
    def excellent_count(self):
        return self._excellent_count
