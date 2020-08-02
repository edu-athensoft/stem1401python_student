"""

"""

"""
Part 3. Solution
1. Please briefly describe when to use the collection type of list and tuple (5’)
When we need to read and write an ordered sequence, we may use the datatype of list.
When we need to read and manipulate on write-protected ordered sequence, we may use the datatype of tuple.

2. Please briefly describe when to use the collection type of set and dictionary (5’)
When we do not care about the order of a collection and do not need duplicated items, we may use the datatype of set.
When we need to do mathematical set operations, we may use the datatype of set.
When we care about the mapping relationship between key-value pairs, we may use the datatype of dictionary.
When we need to search in a large amount of key-value pair dataset within constant time, we may use the datatype of dictionary.

3. Please briefly describe what factors may affect the quality of programs (5’)
coding rules and conventions
architecture or program structure
data structure
algorithms
documentation

4. Can we directly perform comparison for equality with two floating numbers? Why? (5’)
Generally not.
Because a floating number cannot be exactly and absolutely precisely represented in modern computer systems.  There exists precision lost. 

5. What is the difference between a multi-module program and a multi-package program? (5’)
A multi-module program means a program may consist of multiple python modules(files).
A multi-package program means the python modules(files) of a program can be organized into packages, and each package usually holds related modules(files) for a specific topic.

Modules are used to control the size of a python file under the principle of separation.
Packages are used to manage and organize python files at a higher level under the principle of separation.

6. List all variations of syntax for exception handling? Briefly describe why we need exception handling. (5’)

The exception handling may help to avoid crushing when a program runs into a non fatal error.
The exception handling may detect a block of code where errors may occur and programmers do not need to explicitly specify or predict where an error would occur.
The exception handling makes it possible to elegantly close and release resources when errors occur.

structure: 	1-try, 1..n-except, 0..1-else, 0..1-finally

try:
	pass 		# try block
except:
	pass		# except block
else:
	pass		# else block
finally:
	pass		# try block


7. What are the drawbacks of recursive function?  (5’)
Recursive function may cause crushing due to the limited recursion depth.
Recursive function may cause performance issues due to its duplicated calculating for each round of recursion.
Generally, it consumes relatively more space and time.

8. What is a 'magic number' or 'magic value'? Why should we avoid writing them in our programs? How to solve the problem to avoid writing them? (5’)
A magic number or magic value is a raw data(literal) directly used in programs which is always without any comment or description.

Magic numbers or magic values usually result in lower readability, understandability and maintainability of programs.

In order to avoid using magic numbers and values, we may use identifiers (variables) to declare before we use it. A necessary comment may be also of some help.


9. What is the basic process to produce a software? (5’)
Planning -> Requirement -> Analysis and design -> Implementation -> Testing -> Deployment
The process is incremental and may span multiple iterations.

10. How to make your program readable, understandable and maintainable? (5’)
Strictly stick to coding rules and conventions including naming conventions
Using comment and documentation properly
Apply good structure (package, module, function, class)
Try to write generic codes for different cases to improve flexibility so to make it maintainable

"""