import random
word_list = ["niggaswat", "monkey", "roblox"]

# To choose random words from the list
chosen_word = random.choice(word_list).lower()
print(chosen_word)

# (1) Check if the letter is correct by checking each letters in the chosen_word
# (2) Replace the amount of letters (#) from chosen_words to blanks
placeholder = "" # Blanks holder
word_length = len(chosen_word) # Number of letters; roblox = 6
for length in range(word_length):
    placeholder += "_"
print(placeholder)

# Ask the user to guess a letter for the word until all is correct
game_over = False
correct_letters=[]
while not game_over:
   guess = input("Guess the letter: ").lower()

# Place a display that replace blanks for the correct letter
   display = ""
   for letter in chosen_word:
       if letter == guess:
         display += letter
         correct_letters.append(guess)
       elif letter in correct_letters:
         display += letter
       else:
         display += "_"

   print(display)
   if "_" not in display:
       game_over = True
       print("You won!")