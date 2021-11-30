import random
#solution one of creating a list of random numbers in a particular range.
a=random.sample(range(1,20),10)
#solution two of creating a list of random numbers in a particular range.
b=[random.randint(1,20) for i in range(15)]
listOverlap=[i for i in a if i in b]
print(listOverlap)
a=set(a)
b=set(b)
c=a.intersection(b)
print(c)