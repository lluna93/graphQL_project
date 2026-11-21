
import strawberry


@strawberry.input
class CreateEmployeeInput:
    name: str
    position: str
    pay: int


@strawberry.input
class UpdateEmployeeInput:
    id: int
    name: str | None = None
    position: str | None = None
    pay: int | None = None
