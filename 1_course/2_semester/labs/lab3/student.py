"""
Author: Maxym Koval (Group K-12)
"""

from subject import Subject


class Student:
    def __init__(self, transcript_id, group_id=None, name=None, surname=None, patronymic=None):
        # Чи потрібно перевіряти обмеження на ім'я і тд
        self._transcript_id = transcript_id
        self._group_id = group_id
        self._name = name
        self._surname = surname
        self._patronymic = patronymic
        self._rating = 0
        self._mark_sum = 0
        self._doubts_count = 0
        self._excellent_count = 0
        self._subjects = []

    def update(self, subject_name: str, total_points: int, mark: int, exam_points: int):
        # Чи підходить ця назва методу (раніше була така, як і у додатковому фалі до ЛР3 - load)
        if (subject := self.find(subject_name)) is None:
            subject = self.add(subject_name)
        self._excellent_count += (mark == 5)
        self._mark_sum += mark if mark > 1 else 2
        self._rating = self._mark_sum / len(self._subjects)
        self._doubts_count += subject.update(total_points, mark, exam_points)

    def find(self, subject_name: str) -> Subject:
        try:
            sub_index = self._subjects.index(Subject(subject_name))
            return self._subjects[sub_index]
        except ValueError:
            return None

    def add(self, subject_name: str) -> Subject:
        self._subjects.append(Subject(subject_name))
        return self._subjects[-1]

    def subjects2output(self, stream):
        self._subjects.sort(key=lambda subject: (subject.subject_name, subject.total_points))
        res = ""
        for subject in self._subjects:
            res += f"\t{subject.subject_name}\t{subject.total_points}\t{subject.mark}\n"
        stream.write(res)

    def __eq__(self, other):
        return self.transcript_id == other.transcript_id

    @property
    def transcript_id(self):
        return self._transcript_id

    @property
    def group_id(self):
        return self._group_id

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def patronymic(self):
        return self._patronymic

    @property
    def rating(self):
        return self._rating

    @property
    def doubts_count(self):
        return self._doubts_count

    @property
    def excellent_count(self):
        return self._excellent_count
