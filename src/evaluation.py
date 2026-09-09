"""Evaluation helpers used by the consistency-rule experiments."""


def calculate_rule_metrics(valid_count, total_count):
    """
    Return support, coverage, and confidence using the convention employed
    throughout the original MSc notebook.

    In many experiments, coverage and confidence share the same denominator.
    Rule-specific experiments may use different denominators and should keep
    their original calculations in the notebook.
    """
    support = valid_count
    ratio = valid_count / total_count if total_count else 0
    return {
        "support": support,
        "coverage": ratio,
        "confidence": ratio,
    }
