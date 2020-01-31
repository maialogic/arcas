from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from app.api.schema import schema


def get_app() -> FastAPI:
    app = FastAPI()

    app.add_route("/", GraphQLApp(schema=schema))

    return app


app = get_app()
