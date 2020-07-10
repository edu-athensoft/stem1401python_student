"""
For July 9th, 2020.
stem1402_python_homework_5_ken
Ken
"""

# Fibonacci sequence Kevin style

def fibonacci(position):
    """
    Will find fibonacci number at the position in the sequence.
    Uses the function itself to find the answer.
    Goes back to the 3rd number in the sequence : 2 (1+1) and finds all the fibonacci numbers one by one with every iteration.
    :param position: position of the number
    :return: fibonacci number the position
    """
    if position < 0:
        return "error"
    elif position == 0:
        return 0
    elif position == 1 or position == 2:
        return 1
    else:
        for number in range(position):
            return fibonacci(position-1) + fibonacci(position-2)



print(fibonacci(10))

