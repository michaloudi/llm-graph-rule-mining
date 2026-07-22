# LLM-Graph-Rule-Mining

Applying LLMs to Infer Consistency Rules in Property Graph Data.


![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Neo4j](https://img.shields.io/badge/Neo4j-Graph%20Database-green)
![GPT-4](https://img.shields.io/badge/Model-GPT--4-purple)
![LLMs](https://img.shields.io/badge/AI-Large%20Language%20Models-orange)
![Graph Mining](https://img.shields.io/badge/Research-Graph%20Mining-yellow)
![Status](https://img.shields.io/badge/Status-Research%20Project-lightgrey)

## Overview

Property graph databases are widely used to represent complex and interconnected data in domains such as social networks, entertainment platforms, and knowledge-based systems. However, maintaining data consistency often depends on manually defined integrity constraints, which can be time-consuming, difficult to scale, and expensive to maintain.

This repository uses Large Language Models, specifically GPT-4, to infer consistency rules from property graph schemas and graph instances. Graph structures are transformed into textual representations that can be processed by the language model through zero-shot and few-shot prompting.

The generated rules are translated into Cypher queries and evaluated against Neo4j graph databases using three ranking measures: Support, Coverage, and Confidence. Experiments are conducted on Twitter and Movie property graph datasets.

## Features

- Graph-to-text encoding of property graph schemas and database instances
- Zero-shot prompting for consistency-rule generation
- Few-shot prompting with representative rule examples
- Automatic generation of consistency rules using GPT-4
- Automatic translation of natural-language rules into Cypher queries
- Validation of generated rules against Neo4j graph databases
- Rule evaluation using:
  - Support
  - Coverage
  - Confidence
- Experiments on:
  - Twitter property graph
  - Movie property graph
## Architecture

```text
Neo4j Property Graph
        ↓
Graph Encoder
        ↓
JSON/Text Representation
        ↓
Prompt Construction
        ↓
GPT-4
        ↓
Consistency Rules
        ↓
Cypher Query Generator
        ↓
Neo4j Rule Validation
        ↓
Support · Coverage · Confidence
- Visualisation of rule-ranking
```
## Pipeline

The proposed framework follows the pipeline below:

### 1. Load the Property Graph
Load the property graph from the Neo4j database, including node labels, relationship types, node properties, and graph structure.

### 2. Encode the Graph
Transform the graph schema and graph instances into a structured textual representation that can be processed by a Large Language Model.

### 3. Construct the Prompt
Combine the encoded graph with a carefully designed prompt (Zero-shot or Few-shot) requesting the generation of graph consistency rules.

### 4. Query the Large Language Model
Submit the prompt to GPT-4 and obtain consistency rules expressed in natural language.

### 5. Extract Candidate Rules
Parse the LLM response and collect all generated consistency rules.

### 6. Translate Rules into Cypher
Convert each natural-language consistency rule into an executable Cypher query.

### 7. Validate Rules on Neo4j
Execute the generated Cypher queries against the original graph database to identify valid and violating graph instances.

### 8. Compute Evaluation Metrics
Evaluate every generated rule using:
- Support
- Coverage
- Confidence

### 9. Rank and Analyse the Rules
Rank the inferred consistency rules according to the computed metrics and analyse their quality and usefulness.


## Datasets

The experiments were conducted on two property graph datasets with different sizes and structural characteristics: a Twitter network graph and a Movie graph.

### Twitter Network Graph

The Twitter property graph represents social-media entities and interactions.

- **Nodes:** 43,325
- **Relationships:** 57,896
- **Main node types:** User, Tweet, Hashtag, Link, and Source
- **Main relationship types:** POSTS, FOLLOWS, MENTIONS, TAGS, CONTAINS, USING, RETWEETS, and REPLY_TO

The purpose of this dataset is to investigate whether an LLM can infer structural and semantic consistency rules from a relatively large and heterogeneous social-network graph.

Examples of rules include:

- Every Tweet should be posted by an existing User.
- Every Tweet should have a unique identifier.
- A User should not follow themselves.
- A Tweet mentioning a User should contain a corresponding `MENTIONS` relationship.

### Movie Graph

The Movie property graph represents movies, people, professional roles, reviews, and social relationships.

- **Nodes:** 171
- **Relationships:** 253
- **Main node types:** Person and Movie
- **Main relationship types:** ACTED_IN, DIRECTED, PRODUCED, WROTE, REVIEWED, and FOLLOWS

The purpose of this dataset is to examine whether an LLM can infer logical, structural, uniqueness, and temporal constraints from a smaller domain-specific graph.

Examples of rules include:

- A Movie should be associated with at least one Person.
- A Person's birth year should precede the release year of a Movie in which they acted.
- A Person should have only one birth year.
- A Movie should have a consistent title and release year.


