"""Neo4j connection and query helpers."""

from neo4j import GraphDatabase, basic_auth


def create_driver(uri, username, password, encrypted=True):
    """Create a Neo4j driver using credentials supplied outside the repository."""
    return GraphDatabase.driver(
        uri,
        auth=basic_auth(username, password),
        encrypted=encrypted,
    )


def run_query(tx, query, parameters=None):
    """Execute a Cypher query inside an existing transaction."""
    result = tx.run(query, parameters or {})
    return [record.data() for record in result]


def scalar_query(tx, query, key, parameters=None):
    """Execute a Cypher query that returns a single scalar value."""
    result = tx.run(query, parameters or {})
    record = result.single()
    return None if record is None else record[key]
