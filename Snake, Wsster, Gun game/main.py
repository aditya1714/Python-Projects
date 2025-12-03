import random

'''
 1 = sanke 
-1 = water 
 0 = gun
'''

computer = random.choice([1, -1, 0])
youStr = input("enter your choice : ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youStr]

print(f"Computer choosed {reverseDict[computer]}\nYou choosed {reverseDict[you]}")

if(computer == you):
    print("It's Draw")
else:
    if(computer == 1 and you == -1):
        print("You Lose")
    elif(computer == 1 and you == 0):
        print("You Win")
    elif(computer == -1 and you == 1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("You Lose")
    elif(computer == 0 and you == -1):
        print("You Win")
    elif(computer == 0 and you == 1):
        print("You Lose")
    else:
        print("Something went wrong")