fruit = raw_input("Give me a fruit").split(',')
print fruit

#float_fruit = []
def fruit_pluralizer(list_of_strings):
    for x in list_of_strings:
        if x[len(x)-1] == "y":
            print x[:len(x)-1] + 'ies'
            # print fruit_list
        else:
            print x[:len(x)] + 's'
            # print fruit_list
fruit_pluralizer(fruit)
