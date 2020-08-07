print("Hello, and welcome to Hangman! I'm glad you can play...All you have to do is guess letters! If the letter is in the word I have in mind...GREAT! However, if it isn't, then you will get part of the body of my man. If you build the whole man before you guess my word...you lose! However if you guess my word...you win! Good luck and feel free to leave at any time!")
print("WARNING!!! You only have six guesses, the head, body, two arms and two legs. If you guess six guesses wrong, you lose!")
print(" O ")
print("/|\ ")
print("/ \ ")

import random 

words = [] 

with open("words.txt", "r") as f:
  for line in f.readlines(): 
    words.append(line.strip()) 

secret_word = random.choice(words)

correct_guessed = ""
incorrect_guessed = ""

print("This is the amount of letters in my word:") 
letters = len(secret_word) 
print(letters)

lives = 6
gameover = False 
while not gameover and set(correct_guessed) != set(secret_word): 
  guess = input("Guess a letter: ") 
  if guess in secret_word:
    correct_guessed += guess
    print("Correct!")
    for letter in secret_word:
      if letter in correct_guessed: 
          print(letter, end = " ") 
      else:
         print("_", end = " ")
    print("") 
  else: 
    incorrect_guessed += guess
    print("Sorry, that's not in the word!")
    print("Guessed letters that are incorrect: "+" , ".join(sorted(incorrect_guessed))) 
    lives -= 1 
    if lives == 5:
      print(" O ")
    elif lives == 4: 
      print(" O ")
      print(" | ")
    elif lives == 3: 
      print(" O ")
      print("/|")
    elif lives == 2: 
      print(" O ")
      print("/|\ ")
    elif lives == 1: 
      print(" O ")
      print("/|\ ")
      print("/ ")
    elif lives == 0: 
      print(" O ")
      print("/|\ ")
      print("/ \ ")
    if lives > 0: 
     gameover = False  
    else:  
     gameover = True 
     print ("Gameover! Sorry, you ran out of guesses!!! :( The scret word was...")
     print(secret_word)  
if lives > 0: 
 print("YAY! You guessed the word, without running out of guesses!!!") 

