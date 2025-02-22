def function_with_error_handling(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif b < 0:
            raise ValueError("b must be non-negative")
        else:
            return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return float('inf') #Or handle differently
    except ValueError as e:
        print(f"Error: {e}")
        return None # Or handle differently
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None