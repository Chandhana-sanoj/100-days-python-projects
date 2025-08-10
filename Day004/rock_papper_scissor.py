# This code implements a simple Rock, Paper, Scissors game where the user can choose their move,
# and the computer randomly selects its move. The game then determines the outcome based on the rules      



rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_choise= int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_choise == 0:
    print(rock)
elif user_choise == 1:
    print(paper)        
elif user_choise == 2:
    print(scissors) 
else:
    print("Invalid choice. Please choose 0, 1, or 2.")  
    
import random   

computer_choice = random.randint(0, 2)
if computer_choice == 0:            
    print("Computer chose Rock:")
    print(rock) 
elif computer_choice == 1:
    print("Computer chose Paper:")
    print(paper)        
elif computer_choice == 2:
    print("Computer chose Scissors:")
    print(scissors) 
    
if user_choise == computer_choice:
    print("It's a draw!")
elif (user_choise == 0 and computer_choice == 2) or \
     (user_choise == 1 and computer_choice == 0) or \
     (user_choise == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
