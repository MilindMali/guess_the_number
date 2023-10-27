from art import logo

print(logo)

import random

easy_level_turn=10
hard_level_turn=5

def set_difficulty():
  level=input("Choose level of difficulty, type 'easy' or 'hard':")
  if level=='easy':
    return easy_level_turn
  else:
    return hard_level_turn

def check_ans(guess,answer,turns):
  if guess>answer:
    print("Guess is to high")
    return turns-1
  elif guess < answer:
    print("Guess is to low")
    return turns-1
  else:
    print(f"you got it, the answer was {answer}")


def game():
  print("Welocome to number guessing game")
  print("Number will be between 1 to 100")
  
  answer=random.randint(1,100)
  print(answer)

  turns=set_difficulty()
  
  guess=0
  while guess != answer:
    print(f"you have {turns} attempts remained to guess the number")
  
    guess=int(input("Make the guess:\n"))
    turns=check_ans(guess,answer,turns)
    if turns==0:
      print("Sorry !!!, you are running out of guesses, you loose!")
      return
    elif guess != answer:
      print('guess again')

game()
