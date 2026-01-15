import sys
from pathlib import Path

# Add src to import path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from smoothie import smoothie


def test_default_base_and_ice():
    result = smoothie(["banana", "yogurt", "strawberry"])
    assert result.startswith("Icy Water smoothie with ")
    assert "banana" in result
    assert "strawberry" in result
    assert "yogurt" in result


def test_alphabetical_order_case_insensitive():
    result = smoothie(["Strawberry", "banana"])
    # check order without strict full equality
    assert "banana" in result and "strawberry" in result
    assert result.index("banana") < result.index("strawberry")


def test_custom_base_no_ice():
    result = smoothie(["mango", "spinach"], base="almond milk", ice=False)
    assert result.startswith("Almond Milk smoothie with ")
    assert "mango" in result
    assert "spinach" in result
    assert "Icy" not in result


def test_ingredients_must_be_non_empty():
    result = smoothie([])
    assert "don't know how to make" in result.lower()


def test_non_string_ingredient_rejected():
    result = smoothie(["apple", 5])
    assert "don't know how to make" in result.lower()


def test_base_empty_string_falls_back_to_water():
    result = smoothie(["kiwi", "pear"], base="  ", ice=False)
    assert result.startswith("Water smoothie with ")
    assert "kiwi" in result
    assert "pear" in result


def test_duplicates_are_kept_and_sorted():
    result = smoothie(["banana", "banana", "yogurt"])
    assert result.startswith("Icy Water smoothie with ")
    # duplicates kept
    assert result.count("banana") == 2
    # and sorted (banana before yogurt)
    assert result.index("banana") < result.index("yogurt")


def test_show_output_example():
    result = smoothie(["banana", "strawberry", "yogurt"])
    print(result)
    assert "banana, strawberry, yogurt" in result
