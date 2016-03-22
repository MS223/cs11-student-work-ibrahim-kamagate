
for groot in range (1,101):
    if groot % 3 ==0:
        print "fizz"
    elif groot % 5 ==0:
        print "buzz"
    elif groot % 5==0 + groot % 3==0:
        print "fizzbuzz"
    else:
        print groot
