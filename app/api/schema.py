from graphene import Schema
from app.api.queries import Query

schema = Schema(query=Query)
