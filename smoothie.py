def smoothie(ingredients: list[str], base: str = "water", ice: bool = True) -> str:
    """
    Create a smoothie!

    Returns a description of the smoothie with ingredients listed in alphabetical order.

    Args:
        ingredients (list of str): List of ingredients (must be non-empty).
        base (str): The liquid base for the smoothie (default: water).
        ice (bool): Whether to include ice.

    Returns:
        str: A description of the smoothie.
    """
    # base normalization (default: water)
    base_str = (base or "").strip()
    if base_str == "":
        base_str = "water"

    # ingredients must be non-empty list of strings
    if not ingredients or not all(isinstance(i, str) for i in ingredients):
        return "I don't know how to make that smoothie!"

    # normalize ingredients (keep duplicates, only trim + lower)
    cleaned = [i.strip().lower() for i in ingredients]
    if any(i == "" for i in cleaned):
        return "I don't know how to make that smoothie!"

    cleaned.sort()  # alphabetical

    ice_prefix = "Icy " if ice else ""
    return f"{ice_prefix}{base_str.title()} smoothie with " + ", ".join(cleaned)
