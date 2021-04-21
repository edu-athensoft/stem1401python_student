"""
fibonacci number sequence

1,1,2,3,5,8

i(n) = i(n-1) + i(n-2)
"""

"""
i(1) = 1
i(2) = 2
i(3) = 3
"""

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

terms = 5
terms = 20

if terms <= 0:
   print("invalid")
else:
   print("Fibonacci sequence:")
   # for i in range(terms):
   for i in range(1, terms+1):
       print(fibonacci(i))



