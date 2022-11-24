import random
user=input("")
game=("rock","paper","scissor")
pc=random.choice(game)
print(pc)
if user is rock and pc is rock:
    print("Tie")
else:
    print("False") 