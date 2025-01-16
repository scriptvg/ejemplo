# FILE: /scientific-calculator/scientific-calculator/src/utils/__init__.py
def is_number(value):
    """Check if the value is a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False