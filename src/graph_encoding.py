"""Graph loading, cleaning, encoding, and chunking helpers."""

import json
import re
from pathlib import Path

import networkx as nx


def clean_json(raw_json: str) -> str:
    """Remove control characters that can prevent JSON parsing."""
    return re.sub(r"[\x00-\x1f\x7f-\x9f]", "", raw_json)


def load_graph_export(path, clean: bool = True):
    """Load a Neo4j-style JSON graph export from disk."""
    path = Path(path)
    raw = path.read_text(encoding="utf-8-sig")
    if clean:
        raw = clean_json(raw)
    return json.loads(raw)


def build_directed_graph(graph_data):
    """Convert the notebook's Neo4j export format to a NetworkX DiGraph."""
    graph = nx.DiGraph()

    for entry in graph_data:
        n_node = entry["n"]
        m_node = entry["m"]
        relationship = entry["r"]

        graph.add_node(
            n_node["identity"],
            labels=n_node.get("labels", []),
            **n_node.get("properties", {}),
        )
        graph.add_node(
            m_node["identity"],
            labels=m_node.get("labels", []),
            **m_node.get("properties", {}),
        )
        graph.add_edge(
            relationship["start"],
            relationship["end"],
            type=relationship["type"],
            **relationship.get("properties", {}),
        )

    return graph


def split_text(text: str, max_length: int = 2000):
    """Split encoded graph text at newline boundaries where possible."""
    chunks = []
    while len(text) > max_length:
        idx = text.rfind("\n", 0, max_length)
        if idx == -1:
            idx = max_length
        chunks.append(text[:idx])
        text = text[idx:]
    chunks.append(text)
    return chunks
