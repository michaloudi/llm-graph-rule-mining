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
Candidate Consistency Rules
        ↓
Cypher Query Generator
        ↓
Neo4j Rule Validation
        ↓
Support · Coverage · Confidence
- Visualisation of rule-ranking results
