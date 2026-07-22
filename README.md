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

## Project Structure

```text
llm-graph-rule-mining/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── data/
│   ├── twitter/
│   └── movies/
│
├── prompts/
│   ├── zero_shot/
│   ├── few_shot/
│   └── cypher_generation/
│
├── src/
│   ├── graph_loader.py
│   ├── graph_encoder.py
│   ├── prompt_builder.py
│   ├── llm_client.py
│   ├── rule_parser.py
│   └── cypher_generator.py
│
├── evaluation/
│   ├── support.py
│   ├── coverage.py
│   ├── confidence.py
│   └── rule_ranking.py
│
├── results/
│   ├── twitter/
│   ├── movies/
│   └── summary_tables/
│
├── figures/
│
├── notebooks/
│   └── demo.ipynb
│
└── paper/
    └── thesis.pdf
```

### Directory Description

- **`data/`**  
  Contains the graph datasets, graph exports, schemas, and sample files used in the experiments.

- **`prompts/`**  
  Contains the zero-shot, few-shot, and Cypher-generation prompt templates.

- **`src/`**  
  Contains the main Python implementation for loading graphs, encoding graph structures, constructing prompts, querying the LLM, parsing generated rules, and producing Cypher queries.

- **`evaluation/`**  
  Contains the code used to calculate Support, Coverage, Confidence, and rule-ranking results.

- **`results/`**  
  Stores generated consistency rules, Cypher queries, metric values, and experiment outputs for the Twitter and Movie datasets.

- **`figures/`**  
  Contains architecture diagrams, graph visualisations, and evaluation charts.

- **`notebooks/`**  
  Contains demonstration and exploratory notebooks.

- **`paper/`**  
  Contains the thesis report or a future paper version of the project.

### 10. Report the Results
Present the generated rules, Cypher queries, evaluation metrics, tables and visualisations.
 results
