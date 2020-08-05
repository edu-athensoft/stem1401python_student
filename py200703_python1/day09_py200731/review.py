"""
review

"""


num = 123

# create a variable
a = 0

abc =  123
# mutable (changeable)
mylist1 = ['abc',True,345435,412244,54345,6342346,767657]

print(mylist1[0])
print(mylist1[1])
print(mylist1[2])
print(mylist1[3])

mylist1[0] = 'abcd'
print(mylist1)

# read-only,  immutable (unchangeable)
mytuple1 = ('abc',True,11,412244,11,6342346,767657)
print(mytuple1[0])
print(mytuple1[1])
print(mytuple1[2])
print(mytuple1[3])

# mytuple1[0] = 'abcd'
# print(mytuple1)


set1 = {'1','2','3'}
print(set1)

set1 = {'1','1','2','2','3','3','3'}
print(set1)

set1 = {1,1,2,2,3,3,3}
print(set1)

student_profile = {
    'stuno': 201909090001,
    'fname': 'Peter',
    'lname': 'White',
    'groupno': 'G1909-12',
    'coordiator':'Jason',
    'transcript':[90,80,85,69]
}

print(student_profile)
print(student_profile['stuno'])
print(student_profile['transcript'])
