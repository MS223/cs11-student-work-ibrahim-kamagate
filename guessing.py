score = 1
user = raw_input("What is your name ")
number = input("Give me the biggest number that you want to guess")
import random
random =random.randint(1,number )#it choosie the random number 
guess = input("What's your guess?")
while guess != random:#when the user get the number wrong the it goes to the loop
    if guess < random:
        print "Too low"
        guess = input("What's your guess?")
        score = score + 1
    else:
        print "Too high"
        guess = input("What's your guess?")
        score = score + 1
print "You got it right!!!"
print "It took you " + str(score) + " tries " + user
