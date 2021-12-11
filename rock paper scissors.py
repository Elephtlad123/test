import time
import random

print("Welcome to rock paper scissors")
time.sleep(1)
print("this is a game of first to 5")
time.sleep

playerscore = 0
computerscore = 0

while True:
    computer = random.choice(["rock","paper","scissors"])
    player = input("rock paper or scissors?\n")

    if computer == "rock":
        print("the computer picked ",computer)
        time.sleep(1)
        if player == "rock":
            print("you tied")
            time.sleep(1)
            playerscore = playerscore + 0
            computerscore = computerscore + 0
            print("your score is ",playerscore)
            print("the computer score is ",computerscore)
            time.sleep(2)
        if player == "paper":
            print("you win")
            time.sleep(1)
            playerscore = playerscore + 1
            computerscore = computerscore + 0
            print("your score is ",playerscore)
            print("the computers score is ",computerscore)
            time.sleep(2)
        if player == "scissors":
            print("you lose")
            time.sleep(1)
            playerscore = playerscore + 0
            computerscore = computerscore + 1 
            print("your score is ",playerscore)
            print("computers score ",computerscore)
            time.sleep(2) 
    
    if computer == "scissors":
        print("the computer picked ",computer)
        time.sleep(1)
        if player == "rock":
            print("you win")    
            time.sleep(1)
            playerscore = playerscore + 1
            computerscore = computerscore + 0
            print("your score is ",playerscore)
            print("the computers score is ",computerscore)
            time.sleep(2)
        if player == "paper":
            print("you lose")
            time.sleep(1)
            playerscore = playerscore + 0
            computerscore = computerscore + 1
            print("yours score is ",playerscore)
            print("the computer score is ",computerscore)
            time.sleep(2)
        if player == "scissors":
            print("you tied")
            playerscore = playerscore + 0
            computerscore = computerscore + 0
            print("your score is ",playerscore)
            print("the computer score ",computerscore)
            time.sleep(2)

    if computer == "paper":
        print("the computer picked ",computer)
        if player == "rock":
            print("you lose")
            time.sleep(1)
            playerscore = playerscore + 0
            computerscore = computerscore + 1 
            print("your score is ",playerscore)
            print("the computer score ",computerscore)
            time.sleep(2)
        if player == "paper":
            print("you tied")
            time.sleep(1)
            playerscore = playerscore + 0
            computerscore = computerscore + 0 
            print("your score is ",playerscore)
            print("the computers score is ",computerscore)
            time.sleep(2)
        if player == "scissors":
            print("you win")
            time.sleep(1)
            playerscore = playerscore + 1
            computerscore = computerscore + 0
            print("your score is ",playerscore)
            print("the computers score is ",computerscore)
            time.sleep(2)

    if playerscore == 5:
        print("you beat the computer!!!!")
        time.sleep(1)
        break
    if computerscore == 5:
        print("the computer beat you")
        time.sleep(1)
        break