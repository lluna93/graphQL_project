
from sqlalchemy.orm import Session

from app.repository.employee_model import (
    Employee,
    Department,
    Project,
    Evaluation
)


def seed_employees(db: Session):

    # 부서 데이터
    department_names = ["개발팀", "데이터팀", "기획팀"]

    departments = {}

    for name in department_names:
        department = (
            db.query(Department)
            .filter_by(name=name)
            .first()
        )

        if department is None:
            department = Department(name=name)
            db.add(department)
            db.flush()

        departments[name] = department

    # 프로젝트 데이터
    project_titles = [
        "AI 추천",
        "RAG",
        "GraphQL API",
        "데이터 분석",
        "서비스 기획"
    ]

    projects = {}

    for title in project_titles:
        project = (
            db.query(Project)
            .filter_by(title=title)
            .first()
        )

        if project is None:
            project = Project(title=title)
            db.add(project)
            db.flush()

        projects[title] = project

    # 직원별 관계 데이터
    data = [
        ("이순신", "장군", 5000000, "개발팀",
         ["AI 추천", "RAG"], 95),

        ("강감찬", "장군", 4500000, "개발팀",
         ["GraphQL API"], 90),

        ("홍길동", "개발자", 4000000, "데이터팀",
         ["데이터 분석"], 88),

        ("전우치", "기획자", 3800000, "기획팀",
         ["서비스 기획"], 92)
    ]

    for name, position, pay, dept, project_list, score in data:

        employee = (
            db.query(Employee)
            .filter_by(name=name)
            .first()
        )

        if employee is None:
            employee = Employee(
                name=name,
                position=position,
                pay=pay
            )
            db.add(employee)
            db.flush()

        employee.department = departments[dept]

        for title in project_list:
            project = projects[title]

            if project not in employee.projects:
                employee.projects.append(project)

        # 평가 데이터 중복 방지
        if not employee.evaluations:
            employee.evaluations.append(
                Evaluation(score=score)
            )

    db.commit()
