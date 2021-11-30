import random
def listFirstSecond(list):
    print(list)
    end=len(list)-1
    new_list=[list[0],list[end]]
    print(new_list)
    
list=random.sample(range(1,9),5)
listFirstSecond(list)