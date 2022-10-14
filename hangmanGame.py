import random


# STEPS:
# 
# - Generate a random word
# - ask player to guess letter
#
# - Guess correct:
# -- Allow player to continue guessing
# -- When complete, congratulate
# 
# - Guess wrong:
# -- player looses a life
# -- Initial number of lives is = lenght of word##

words = ["football", "ronaldo", "messi", "halaand", "devops", "cloud", "infrastructure", "money"]

# - Generate a random word
pos = random.randint(0, len(words));

secret = words[pos]

# print(f"psst! The word is {secret}") #for debugging

lives = len(secret)
blanksLeft = len(secret)
guessSheet = []
secretLength = len(secret)

for _ in range(secretLength):
        guessSheet += "_"


# - ask player to guess letter

print(f"You have {lives} lives left")
print(guessSheet)

while lives > 0 and blanksLeft > 0:
    guess = input("Guess a letter that makes up the secret word:\n").lower()
    
    checker = False;

    for position in range(secretLength):
        
        if guess == secret[position]:
            guessSheet[position] = guess
            checker = True;
            blanksLeft -= 1

            if blanksLeft == 0:
                print("Congratulation!!! You Won!")
                break

    if checker == False:
        lives -= 1
        print(f"Wrong answer. You now have {lives} lives left")

        if lives == 0:
            print("Off with your head!!! You died...")
            break

    

    print(guessSheet)
            


            









