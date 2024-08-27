def divide_num(a, b):
    """Divide two numbers with exception handling for division by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        return result
    finally:
        print("Operation completed")
