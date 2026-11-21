
from sqlalchemy.orm import Session, selectinload, joinedload
from app.repository.employee_model import Employee


# 직원 전체 조회 + 관계 데이터 로딩
def employees(db: Session):
    return (
        db.query(Employee)
        .options(
            joinedload(Employee.department),
            selectinload(Employee.projects),
            selectinload(Employee.evaluations)
        )
        .order_by(Employee.id)
        .all()
    )


# 직원 단건 조회
def get_employee(db: Session, employee_id: int):
    return (
        db.query(Employee)
        .options(
            joinedload(Employee.department),
            selectinload(Employee.projects),
            selectinload(Employee.evaluations)
        )
        .filter(Employee.id == employee_id)
        .first()
    )


def create_employee(
    db: Session,
    name: str,
    position: str,
    pay: int
):
    employee = Employee(
        name=name,
        position=position,
        pay=pay
    )

    db.add(employee)
    db.commit()

    return get_employee(db, employee.id)


def update_employee(
    db: Session,
    employee_id: int,
    name: str | None = None,
    position: str | None = None,
    pay: int | None = None
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        return None

    if name is not None:
        employee.name = name

    if position is not None:
        employee.position = position

    if pay is not None:
        employee.pay = pay

    db.commit()

    return get_employee(db, employee_id)


def delete_employee(db: Session, employee_id: int):
    employee = db.get(Employee, employee_id)

    if employee is None:
        return False

    db.delete(employee)
    db.commit()

    return True
