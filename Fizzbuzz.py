
for groot in range (1,101):#this is the range of numbers
    if groot % 5==0 + groot % 3==0:# this goes through all the number and see if 5 and 3 dvisble by it 
        print "fizzbuzz"
    elif groot % 5 ==0:# if 5 and 3 isn't divisble by that number then it will check just 5 is divisble by the number
        print "buzz"
    elif groot % 3 ==0::# if 5 isn't divisble by that number then it will check just 3 is divisble by the number
        print "fizz"
    else:#if none of the numbers is divisble by hat number than it will print the number
        print groot
