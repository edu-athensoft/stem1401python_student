"""
anonymous function
lambda function

call-back function
"""

def foo():
    print("foo()")

foo()


"""
syntax
lambda arg1,[arg2, arg3, ....] : expression
"""

# sum of a and b
def add(a, b):
    return a + b

print(add(3,6))


add = lambda x,y : x + y
print(add(3,7))


"""
ajax request

.ajax({
    method: post,
    success: function() {
        alert("Saved.");
    },
    error: function(){
        alert("Failed");
    },
    complete: function(){
        console.log("Complete");
    }
})

"""