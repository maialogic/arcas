from graphene.test import Client
from app.api.schema import schema

client = Client(schema)


def test_hello(snapshot):
    query = """
        {
          hello
        }
    """
    snapshot.assert_match(client.execute(query))
