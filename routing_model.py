def route_prompt(prompt: str):
    score = 0
    reasons = []

    # Feature 1: Prompt length
    if len(prompt) > 50:
        score += 1
        reasons.append("long_prompt")

    # Feature 2: Complex keywords
    complex_words = ["explain", "analyze", "compare", "code", "write"]
    if any(word in prompt.lower() for word in complex_words):
        score += 1
        reasons.append("complex_keywords")

    # Feature 3: Reasoning requirement
    if "why" in prompt.lower() or "how" in prompt.lower():
        score += 1
        reasons.append("reasoning_required")

    # Decision
    if score >= 2:
        return "CAPABLE", 0.85, ",".join(reasons)
    else:
        return "FAST", 0.65, ",".join(reasons)