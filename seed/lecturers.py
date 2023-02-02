from faker import Faker

from database.db import session
from database.models import Lecturer

fake = Faker('uk_UA')


def create_lecturers():
    for _ in range(4):
        lecturer = Lecturer(
            full_name=fake.name()
        )
        # print(f"{lecturer.full_name}")
        session.add(lecturer)
    session.commit()


if __name__ == '__main__':
    create_lecturers()
