from datetime import datetime

from sqlalchemy.orm import joinedload
from sqlalchemy import and_, func, desc

from database.db import session
from database.models import Student, Lecturer, Grades, Sgroup, Subject


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def query_1():
    result = session.query(Student.full_name, func.round(func.avg(Grades.grade), 2).label('avg_grade')) \
        .select_from(Grades).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    print(result)


# Знайти студента із найвищим середнім балом з певного предмета
def query_2():
    result = session.query(Student.full_name, func.round(func.avg(Grades.grade), 2).label("avg_grade"), Subject.subject) \
        .select_from(Grades).join(Student).join(Subject).filter(Subject.subject == "History") \
        .group_by(Student.full_name, Subject.subject).order_by(desc("avg_grade")).limit(1).all()
    print(result)


# Знайти середній бал у групах з певного предмета
def query_3():
    result = session.query(Sgroup.group_name, func.round(func.avg(Grades.grade), 2).label("avg_grade"), Subject.subject) \
        .select_from(Grades).join(Student).join(Sgroup).join(Subject).filter(and_(
            (Sgroup.group_name == "group 2"),
            (Subject.subject == "Biology")
        )).group_by(Sgroup.group_name, Subject.subject).all()
    print(result)


# Знайти середній бал на потоці (по всій таблиці оцінок)
def query_4():
    result = session.query(func.round(func.avg(Grades.grade), 2).label("avg_grade")).select_from(Grades) \
        .order_by(desc('avg_grade')).all()
    print(result)


# Знайти які курси читає певний викладач
def query_5():
    result = session.query(Lecturer.full_name, Subject.subject).select_from(Lecturer).join(Subject) \
        .filter(Lecturer.id == 4).order_by(Lecturer.full_name).all()
    print(result)


# Знайти список студентів у певній групі
def query_6():
    result = session.query(Student.full_name, Sgroup.group_name).select_from(Student).join(Sgroup) \
        .filter(Sgroup.group_name == "group 2").order_by(Sgroup.group_name).all()
    print(result)


# Знайти оцінки студентів у окремій групі з певного предмета
def query_7():
    result = session.query(Sgroup.group_name, Subject.subject, Grades.grade).select_from(Grades) \
        .join(Student).join(Sgroup).join(Subject).filter(and_(
            (Sgroup.group_name == "group 3"),
            (Subject.subject == "Biology"))) \
        .group_by(Grades.grade, Sgroup.group_name, Subject.subject).all()
    print(result)


# Знайти середній бал, який ставить певний викладач зі своїх предметів
def query_8():
    result = session.query(Lecturer.full_name, func.round(func.avg(Grades.grade), 2).label("avg_grade")) \
        .select_from(Grades).join(Lecturer).filter(Lecturer.id == 3).group_by(Lecturer.full_name).all()
    print(result)


# Знайти список курсів, які відвідує певний студент
def query_9():
    result = session.query(Student.full_name, Subject.subject).select_from(Grades) \
        .join(Student).join(Subject).filter(Student.id == 46).group_by(Student.full_name, Subject.subject).all()
    print(result)


# Список курсів, які певному студенту читає певний викладач
def query_10():
    result = session.query(Student.full_name, Subject.subject, Lecturer.full_name).select_from(Grades) \
        .join(Student).join(Subject).join(Lecturer).filter(and_(Student.id == 46), (Lecturer.id == 4)) \
        .group_by(Student.full_name, Lecturer.full_name, Subject.subject).all()
    print(result)


# Середній бал, який певний викладач ставить певному студентові
def query_11():
    result = session.query(func.round(func.avg(Grades.grade), 2), Student.full_name, Lecturer.full_name) \
        .select_from(Grades).join(Student).join(Lecturer).filter(and_(
            (Student.id == 56),
            (Lecturer.id == 4)
        )).group_by(Student.full_name, Lecturer.full_name).all()
    print(result)


# Оцінки студентів у певній групі з певного предмета на останньому занятті
def query_12():
    result = session.query(Grades.grade, Sgroup.group_name, Subject.subject) \
        .select_from(Grades).join(Student).join(Sgroup).join(Subject).filter(and_(
            Sgroup.id == 2,
            Subject.id == 6,
            Grades.date_stump > datetime(year=2023, month=1, day=26)
        )).group_by(Grades, Sgroup, Subject).all()
    print(result)


if __name__ == '__main__':
    query_12()
