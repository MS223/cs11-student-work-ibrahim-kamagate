# number = input("Give me a radom number")
# max_value= range(1, number +1)
# print max_value
list = [1,3,5,7,9]
list1 = [2,4,6,8,10]
def compare_lists(list,list1):
    for x in list:
        if x > list1[list.index(x)]:
            print x
        else:
            print list1[list.index(x)]

compare_lists(list,list1)

