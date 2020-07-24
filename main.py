print("Hello, and welcome to Hangman! I'm glad you can play...All you have to do is guess letters! If the letter is in the word I have in mind...GREAT! However, if it isn't, then you will get part of the body of my man. If you build the whole man before you guess my word...you lose! However if you guess my word...you win! Good luck and feel free to leave at any time!")

import random 

words = [] 

with open("words.txt", "r") as f:
  for line in f.readlines(): 
    words.append(line.strip()) 

secret_word = random.choice(words)

correct_guessed = ""
all_guessed = ""

print("This is the amount of letters in my word:") 
letters = len(secret_word) 
print(letters)

while set(correct_guessed) != set(secret_word):
  if correct_guessed:
    print("Guessed letters that are correct: "+" , ".join(sorted(correct_guessed))) 
  guess = input("Guess a letter: ") 
  all_guessed += guess 
  if guess in secret_word:
    correct_guessed += guess
    print("Correct!")
  else: 
    print("Sorry, that's not in the word!")

print("YAY! You guessed the word!")
