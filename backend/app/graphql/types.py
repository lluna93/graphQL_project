
import strawberry


@strawberry.type
class DepartmentType:
    id: int
    name: str


@strawberry.type
class ProjectType:
    id: int
    title: str


@strawberry.type
class EvaluationType:
    id: int
    score: int


@strawberry.type
class EmployeeType:
    id: int
    name: str
    position: str
    pay: int

    # GraphQL 중첩 조회
    department: DepartmentType | None
    projects: list[ProjectType]
    evaluations: list[EvaluationType]
