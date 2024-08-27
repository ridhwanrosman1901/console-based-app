counter = 0

def increment_counter():
    """Increment the counter by 1."""
    global counter
    counter += 1
    print(f"Increment value: {counter}")

def reset_counter():
    """Reset the counter to 0."""
    global counter
    counter = 0
    print(f"Reset value: {counter}")

def show_counter():
    """Display the current value of the counter."""
    print(f"Global value: {counter}")
