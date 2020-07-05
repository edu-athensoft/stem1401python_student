# 4.
# I don't know how to print a table
for i in range(1,10):
    for x in range(1,i+1):
        print("{}*{}={}".format(x,i,x*i), end="\t")
    print()
