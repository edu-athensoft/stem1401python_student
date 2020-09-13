"""
exception handling

built-in exceptions
user-defined exceptions (user custom exception)

raise an error
    by python interpreter
    by programmer

throw an exception (object)

How it works?
When these exceptions occur, the Python interpreter stops
the current process and passes it to the calling process
until it is handled. If not handled, the program will crash.

How to read error message (traceback)
from bottom to top

"""

"""
Exception process
fc -> fb -> fa -> main program -> python interpreter -> crash

handling exception or error just before python interpreter gets interfered.


"""


def fa():
    fb()

def fb():
    fc()

def fc():
    print("fc")
    raise ValueError("my error")


fa()

