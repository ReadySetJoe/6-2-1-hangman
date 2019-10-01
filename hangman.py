import random

print('Welcome to Hangman!\n\n A word will be chosen at random and you must try to guess it letter by letter before an innocent person is hanged! Good luck!')
keep_going = True

words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
          "computer", "python", "program", "glasses", "sweatshirt",
          "sweatpants", "mattress", "friends", "clocks", "biology",
          "algebra", "suitcase", "knives", "ninjas", "shampoo"
          ]

chosen_word = random.choice(words).lower()
word_so_far = ['-'] * len(chosen_word)
print(word_so_far)
guessed_letters = []
print(chosen_word)

HANGMAN = (
  """
  -----
  |   |
  |
  |
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  |
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  |  -+-
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  |
  |
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | 
  |  | 
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | | 
  |  | 
  |
  --------
  """,
  """
  -----
  |   |
  |   0
  | /-+-\ 
  |   | 
  |   | 
  |  | | 
  |  | | 
  |
  --------
  """)

print(HANGMAN[0])
attempts = len(HANGMAN) - 1
print('Time to play!\n')

while keep_going:
  player_guess = input('Type your guess below:\n')
  if not player_guess.isalpha():
      print("That is not a letter. Please try again.")
      continue
  elif len(player_guess) > 1:
      print("That is more than one letter. Please try again.")
      continue
  elif player_guess in guessed_letters:
      print("You have already guessed that letter. Please try again.")
      continue
  else:
      pass

  for letter in range(len(chosen_word)):
    if player_guess == chosen_word[letter]:
        word_so_far[letter] = player_guess

  if player_guess in chosen_word:
    print(HANGMAN[(len(HANGMAN) - 1) - attempts])
    print('Yes! Congrats!\n')
    
  else:
    attempts -= 1
    guessed_letters.append(player_guess)
    print(HANGMAN[(len(HANGMAN) - 1) - attempts])
  
  print(' '.join(word_so_far))
  print('[',' '.join(guessed_letters),']')
  
  if not attempts or '-' not in word_so_far:
    keep_going = False


if "-" not in word_so_far:
  print(("\nCongratulations! {} was the word").format(chosen_word))
else:
  print(("NOOOOOOOOOO! The word was {}.").format(chosen_word))
  
