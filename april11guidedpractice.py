# what does this function return ? This prints the x*2 which is 7*2
def print_only(x):
   y = x * 2
   print y

# how is this one different ? This does the same thing as the print function but you dont see it
def return_only(x):
   y = x * 2
   return y

# let's try to use our 2 functions
print "running print_only ..."# This prints whatever is in the quotes and it does the equation that is given an gives you the sum
print_only(7)

print "running return_only ..."# It does the samething as the one on line 12 but it doesn't print the sum
return_only(7)

print "printing print_only ..."# adding print mkes it also print none
print print_only(7)

print "printing return_only ..."
return_only(7)

print "using print_only ..."
print_only(7) + 6

print "using return_only ..."
return_only(7) + 6


