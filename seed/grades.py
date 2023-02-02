import random

from faker import Faker

from database.db import session
from database.models import Lecturer, Student, Subject, Grades

fake = Faker('uk_UA')


def create_grades():
    lecturers = session.query(Lecturer).all()
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for _ in range(600):
        lecturer = random.choice(lecturers)
        student = random.choice(students)
        subject = random.choice(subjects)

        grade = Grades(
            grade=random.randint(1, 10),
            date_stump=fake.date_between(start_date="-2y"),
            lecturer_id=lecturer.id,
            student_id=student.id,
            subject_id=subject.id
        )
        # print(f"{grade.grade}: {grade.date_stump}: {grade.lecturer_id}: {grade.student_id}: {grade.subject_id}")
        session.add(grade)
    session.commit()


if __name__ == '__main__':
    create_grades()
