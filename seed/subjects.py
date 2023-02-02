import random

from database.db import session
from database.models import Subject, Lecturer

fake_subjects = ["Chemistry", "Geography", "Geometry", "History", "Literature", "Mathematics", "Biology"]


def create_subjects():
    lecturers = session.query(Lecturer).all()

    for subject in fake_subjects:
        lecturer = random.choice(lecturers)
        subject = Subject(
            subject=subject,
            lecturer_id=lecturer.id
        )
        # print(f"{subject.subject} group id: {subject.lecturer_id}")
        session.add(subject)
    session.commit()


if __name__ == '__main__':
    create_subjects()
