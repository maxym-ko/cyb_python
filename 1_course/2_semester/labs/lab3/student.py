from subject import Subject


class Student:
    # Todo ask about *args (is it ok???)
    def __init__(self, transcript_id, *args):
        self._transcript_id = transcript_id
        if len(args) == 4:
            self._group_id = args[0]
            self._name = args[1]
            self._surname = args[2]
            self._patronymic = args[3]
            self._rating = 0
            self._doubts_count = 0
            self._excellent_count = 0
            self._subjects = []

    def load(self, subject_name: str, total_points: int, mark: int, exam_points: int):
        if (subject := self.find(subject_name)) is None:
            subject = self.add(subject_name)
        self._excellent_count += mark == 5
        self._rating = (self._rating * (len(self._subjects) - 1) + mark) / len(self._subjects)
        self._doubts_count += subject.load(total_points, mark, exam_points)

    def find(self, subject_name: str) -> Subject:
        try:
            sub_index = self._subjects.index(Subject(subject_name))
            return self._subjects[sub_index]
        except ValueError:
            return None

    def add(self, subject_name: str) -> Subject:
        self._subjects.append(Subject(subject_name))
        return self._subjects[-1]

    # Todo: is it ok to have this method?
    def subjects2output(self):
        self._subjects.sort(key=lambda subject: (subject.subject_name, subject.total_points))
        res = ""
        for subject in self._subjects:
            res += f"\t{subject.subject_name}\t{subject.total_points}\t{subject.mark}\n"
        return res

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
