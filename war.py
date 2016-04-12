import random
score = 0
player_name = raw_input("What is player one name?")
player_name1 = raw_input("What is player two name?")
# shuffled_deck: will returna shuffled deck to the user
#input:
#output: a list representing a shuffled deck
def shuffled_deck():
	basic_deck = range(2, 15) * 4
	random.shuffle(basic_deck)
	return basic_deck

deck = shuffled_deck()
def player_turn(player_name):
    card = deck.pop()
    print player_name, 'drew card', card
    return card




# compare_score = player_name, player_name1
# if player_name > player_name1:
#     print player_name + " won"
# elif player_name < player_name1:
#     print player_name1 + " won"
# else:
#     print "Tie"

while len(deck) > 0:
    card = player_turn(player_name)
    card1 = player_turn(player_name1)
    if card > card1:
        print player_name + " won"
    elif card < card1:
        print player_name1 + " won"
    else:
        print "Tie"
