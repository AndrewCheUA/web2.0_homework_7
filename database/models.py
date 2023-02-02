from sqlalchemy import Column, Integer, String, Boolean, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    group_id = Column('group_id', ForeignKey('st_groups.id', ondelete='CASCADE'), nullable=False)

    group = relationship("Sgroup", back_populates="student")

    lecturers = relationship("Lecturer", secondary="grades", back_populates="students",
                             passive_deletes=True)


class Lecturer(Base):
    __tablename__ = "lecturers"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)

    subject = relationship("Subject", back_populates="lecturer")

    students = relationship("Student", secondary="grades", back_populates="lecturers",
                            passive_deletes=True)


class Sgroup(Base):
    __tablename__ = "st_groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(150), nullable=False)

    student = relationship("Student", back_populates="group")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject = Column(String(150), nullable=False)
    lecturer_id = Column(ForeignKey('lecturers.id', ondelete='CASCADE'), nullable=False)

    lecturer = relationship("Lecturer", back_populates="subject")


class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_stump = Column(DateTime, default=func.now())
    lecturer_id = Column('lecturer_id', ForeignKey('lecturers.id', ondelete='CASCADE'), nullable=False)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    subject_id = Column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False)
