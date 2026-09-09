"""LLM helper functions for the original OpenAI 0.28 experimental workflow."""

import openai


def generate_chat_completion(
    prompt,
    model="gpt-4",
    system_message="You are a helpful assistant.",
    max_tokens=500,
    temperature=None,
):
    """Generate one chat completion and return its text."""
    kwargs = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
    }
    if temperature is not None:
        kwargs["temperature"] = temperature

    response = openai.ChatCompletion.create(**kwargs)
    return response.choices[0]["message"]["content"]


def generate_consistency_rules(
    graph_description,
    graph_name="property graph",
    model="gpt-4",
    max_tokens=500,
    temperature=None,
):
    """Generate candidate consistency rules from a textual graph description."""
    prompt = (
        f"The following is a description of a {graph_name}:\n\n"
        f"{graph_description}\n\n"
        "Can you generate some consistency rules that could be detected "
        "in the relationships and interactions within this graph?"
    )
    return generate_chat_completion(
        prompt=prompt,
        model=model,
        system_message="You are an expert in graph data and consistency-rule analysis.",
        max_tokens=max_tokens,
        temperature=temperature,
    )
