import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What would you like to choose? 0 for rock, 1 for paper, 2 for scissors.\n"))
computer = random.randint(0, 2)

if player != 0 <= player > 3:
    print("You entered an Invalid number. You lose")
else:
    if player == 0:
        print(rock)
        print("The computer chose:")
        if computer == 0:
            print(rock)
            print("It's a draw.")
        elif computer == 1:
            print(paper)
            print("You Lose.")
        elif computer == 2:
            print(scissors)
            print("You Win.")

    if player == 1:
        print(paper)
        print("The computer chose:")
        if computer == 0:
            print(rock)
            print("You Win.")
        elif computer == 1:
            print(paper)
            print("It's a draw.")
        elif computer == 2:
            print(scissors)
            print("You Lose.")

    if player == 2:
        print(scissors)
        print("The computer chose:")
        if computer == 0:
            print(rock)
            print("You Lose.")
        elif computer == 1:
            print(paper)
            print("You Win.")
        elif computer == 2:
            print(scissors)
            print("It's a draw")