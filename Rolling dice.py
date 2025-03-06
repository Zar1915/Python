import random
start = str(input("Type Yes to roll the dice!"))
def choice():
    return random.choice(['1', '2','3','4','5','6'])
dice_rolled = choice() 
def rolling_done():
    print(f"the number you rolled is {dice_rolled}")
if start == "Yes":
    rolling_done() 

