"""
infinite loop

condition at the bottom

the body of loop is executed at least once.

do-while


Java
do {

  //....
}while(condition);

"""

counter = 10

while True:
    print("infinite loop")
    counter -= 1

    # conditionally
    if counter <= 0:
        break




