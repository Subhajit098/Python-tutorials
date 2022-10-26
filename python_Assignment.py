# process an infinite loop for the user to give inputs until he/she wins against the computer
# take the computers's input as an random string with the help of random.choice(["rock","paper","scissor"])
# rock>paper & rock>scissor 
# scissor>paper
# Write conditionals for wining and losing against the computer.
import random
computer=["rock","paper","scissor"]
while(True):
    userInput=input("Your choice: ")
    userInput=userInput.lower()
    computer_ans=random.choice(computer)
    if userInput=="" or userInput not in computer:
         print("Invalid Input! Please pass correct some words.Restart the game to play again.")
         continue
         

    print(f"Computer's choice: {computer_ans}")
    if (userInput==computer_ans):
        print("Tie!")
        continue
    elif userInput=="rock" and computer_ans=="scissor":
        print("You Win!")
        break
    elif userInput=="scissor" and computer_ans=="paper":
        print("You Win!")
        break
    elif userInput=="rock"  and computer_ans=="paper":
        print("You Win!")        
        break
    else:
        print("You Lost!")
        continue

