import random

from faker import Faker

from database.db import session
from database.models import Student, Sgroup

fake = Faker('uk_UA')


def create_students():
    groups = session.query(Sgroup).all()

    for _ in range(30):
        group = random.choice(groups)
        student = Student(
            full_name=fake.name(),
            group_id=group.id
        )
        # print(f"{student.full_name} group id: {student.group_id}")
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()
