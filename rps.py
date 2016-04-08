score = 0
#scissors = "scissors" > "paper"
#rock = "rock" > "scissors"
#paper = "paper" > "rock"
import random
list = ['rock', 'paper','scissors']
rounds = input("How many rounds do you want?")
rps = random.choice(list)
game = raw_input("Choose between rock, paper, or scissors: ")
print rps
for x in range(1, rounds):
    if game == rps:
        print "Tie, try again"
        game = raw_input("Choose between rock, paper, or scissors: ")
        print rps

    elif game <  rps:
        print "You lost, try again"
        game = raw_input("Choose between rock, paper, or scissors: ")
        print rps

    else:
        print "you won"
        game = raw_input("Choose between rock, paper, or scissors: ")
        print rps
        score = score + 1

print "You won " + str(score) + " time!"
