
from contextlib import asynccontextmanager

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.database import Base, engine, SessionLocal
from app.repository import employee_model
from app.graphql.resolver import schema
from app.seed import seed_employees


@asynccontextmanager
async def lifespan(app: FastAPI):

    # 테이블 생성
    Base.metadata.create_all(bind=engine)

    # 초기 데이터 생성
    with SessionLocal() as db:
        seed_employees(db)

    yield


app = FastAPI(
    title="Employee GraphQL API",
    lifespan=lifespan
)

app.include_router(
    GraphQLRouter(schema),
    prefix="/graphql"
)


@app.get("/")
def root():
    return {"message": "Employee GraphQL API"}
