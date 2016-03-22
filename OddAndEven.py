list = [3,4,7,13,54,32,653,256,1,41,65,83,92,31]
def find_odds(input): #finding the odd numbers 
    for x in input:
        if x % 2 == 1:
            print (x)
find_odds(list)


def odd_sum(input): #sum of odds
    odd_list=[]
    for x in input:
        if x % 2 == 1:
            odd_list.append(x)
    print  sum(odd_list)

odd_sum(list)


def find_even(input): #finding the even numbers 
    even_list=[]
    for x in list:
        if x % 2 == 0:
            even_list.append(x)
    print (even_list)
find_even(list)
