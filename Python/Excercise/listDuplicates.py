def duplicateOut(list):
    new_list=[]
    for i in list:
        if not i in new_list:
            new_list.append(i)
    return new_list

def duplicateOutSets(list):
    new_list=set()
    for i in list:
        new_list.add(i)
    return new_list

list=[1,1,2,3,2,4,3,4,5,6,10]
print(duplicateOut(list))
print(duplicateOutSets(list))