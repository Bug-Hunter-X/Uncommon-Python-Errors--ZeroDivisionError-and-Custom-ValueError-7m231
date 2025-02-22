def function_with_uncommon_error(a, b):
    if a == 0:
        return 1 / a  # ZeroDivisionError
    elif b < 0:
        raise ValueError("b must be non-negative")
    else:
        return a / b