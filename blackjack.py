import random


my_hand = ("")

delears_hand = ("")

blackjack = (21)

bust = (22)


my_hand = random.randint(1,10) + random.randint(1,10)

delears_hand = random.randint(1,16)

print("This is your hand:",my_hand)

print("This is The Dealears hand:",delears_hand , "?")

print("Do you want to (h) or (s) ")

question = input()

if question == ("h"):
	(delears_hand1) = ("the dealears hand" ,delears_hand + random.randint(1,20))
	(my_hand1) = ("your hand" , my_hand + random.randint(1,10))
	if (my_hand1) > (delears_hand1) or (my_hand1) != (bust):
		print("you win!")
		print("thy is your hand:",my_hand1)
		print("thy is the:" ,delears_hand1)
		if (delears_hand1) == (my_hand1):
			print("Tie!")
			print("thy is your hand:",my_hand1)
			print("thy is the:" ,delears_hand1)
			if (my_hand1) or (delears_hand1) > (bust):
				print("you bust")
				print("thy is your hand:",my_hand1)
				print("thy is the:" ,delears_hand1)

if question ==("s"):
	(delears_hand2) =("the dealears hand" ,delears_hand + random.randint(1,20))
	if (my_hand) > (delears_hand) or (my_hand) == (blackjack):
		print("you win!")
		print("thy is your hand:",my_hand)
		print("thy is the:" ,delears_hand2)
		if (delears_hand2) == (my_hand):
			print("Tie!")
			print("thy is your hand:",my_hand)
			print("thy is the:" ,delears_hand2)
			if (delears_hand2) > (bust):
				print("you bust")
				print("thy is your hand:",my_hand)
				print("thy is the:",delears_hand2)








   




