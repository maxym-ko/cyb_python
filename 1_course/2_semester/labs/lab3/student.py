from subject import Subject


class Student:
    def __init__(self, transcript_id, group_id, name, surname, patronymic):
        self._transcript_id = transcript_id
        self._group_id = group_id
        self._name = name
        self._surname = surname
        self._patronymic = patronymic
        self._rating = 0
        self._doubts_count = 0
        self._subjects = []

    # def __init__(self, transcript_id, *args):
    #     self.transcript_id = transcript_id
    #     if len(args) == 4:
    #         self.group_id = args[0]
    #         self.name = args[1]
    #         self.surname = args[2]
    #         self.patronymic = args[3]
    #         self.rating = 0
    #         self.doubts_count = 0
    #         self.subjects = []

    def load(self, subject_name, total_points, mark, exam_points):
        if (subject := self._find(subject_name)) is None:
            subject = self._add(subject_name)
        self._doubts_count += subject.load(total_points, mark, exam_points)

    def _find(self, subject_name):
        sub_index = self._subjects.index(Subject(subject_name))
        return None if sub_index == -1 else self._subjects[sub_index]

    def _add(self, subject_name):
        self._subjects.append(Subject(subject_name))
        return self._subjects[-1]

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
