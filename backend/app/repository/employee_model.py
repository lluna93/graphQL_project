
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base


# 직원 ↔ 프로젝트: N:M 관계
employee_projects = Table(
    "employee_projects",
    Base.metadata,
    Column(
        "employee_id",
        Integer,
        ForeignKey("employees.id"),
        primary_key=True
    ),
    Column(
        "project_id",
        Integer,
        ForeignKey("projects.id"),
        primary_key=True
    )
)


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    # 부서 1개 → 직원 여러 명
    employees = relationship(
        "Employee",
        back_populates="department"
    )


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    pay = Column(Integer, nullable=False)

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=True
    )

    department = relationship(
        "Department",
        back_populates="employees"
    )

    projects = relationship(
        "Project",
        secondary=employee_projects,
        back_populates="employees"
    )

    evaluations = relationship(
        "Evaluation",
        back_populates="employee"
    )


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    employees = relationship(
        "Employee",
        secondary=employee_projects,
        back_populates="projects"
    )


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    employee = relationship(
        "Employee",
        back_populates="evaluations"
    )
