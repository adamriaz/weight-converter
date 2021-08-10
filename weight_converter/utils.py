def divide_by_zero_check(func):
    """
    Decorator for checking division by zero from user input
    """
    def inner(value):
        if value.value == 0:
            raise ValueError('Cannot divide by zero!')
        return func(value)
    return inner
