
import strawberry

from app.database import SessionLocal
from app.service import employee_service
from app.graphql.types import (
    EmployeeType,
    DepartmentType,
    ProjectType,
    EvaluationType
)
from app.graphql.inputs import (
    CreateEmployeeInput,
    UpdateEmployeeInput
)


# SQLAlchemy Model → GraphQL Type 변환
def to_type(employee):

    department = None

    if employee.department:
        department = DepartmentType(
            id=employee.department.id,
            name=employee.department.name
        )

    projects = [
        ProjectType(
            id=p.id,
            title=p.title
        )
        for p in employee.projects
    ]

    evaluations = [
        EvaluationType(
            id=e.id,
            score=e.score
        )
        for e in employee.evaluations
    ]

    return EmployeeType(
        id=employee.id,
        name=employee.name,
        position=employee.position,
        pay=employee.pay,
        department=department,
        projects=projects,
        evaluations=evaluations
    )


@strawberry.type
class Query:

    @strawberry.field
    def employees(self) -> list[EmployeeType]:
        with SessionLocal() as db:
            result = employee_service.employees(db)
            return [to_type(e) for e in result]

    @strawberry.field
    def employee(self, id: int) -> EmployeeType | None:
        with SessionLocal() as db:
            result = employee_service.get_employee(db, id)
            return to_type(result) if result else None


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_employee(
        self,
        input: CreateEmployeeInput
    ) -> EmployeeType:

        with SessionLocal() as db:
            employee = employee_service.create_employee(
                db,
                input.name,
                input.position,
                input.pay
            )
            return to_type(employee)

    @strawberry.mutation
    def update_employee(
        self,
        input: UpdateEmployeeInput
    ) -> EmployeeType | None:

        with SessionLocal() as db:
            employee = employee_service.update_employee(
                db,
                input.id,
                input.name,
                input.position,
                input.pay
            )
            return to_type(employee) if employee else None

    @strawberry.mutation
    def delete_employee(self, id: int) -> bool:
        with SessionLocal() as db:
            return employee_service.delete_employee(db, id)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
