import random
import string

adjectives = ["stupid", "fat", "ugly", "dry", "tall", "short", "disappointing", "cowardly"]

colours = ["white", "blue", "orange", "green", "brown", "black", "pink", "lime", "yellow"]

nouns = ["goat", "basketball", "egg", "cheese", "pig", "pug", "bread", "manhattan"]
              
print("Welcome to Password Picker!")

while True:

    adjective = random.choice(adjectives)
    colour = random.choice(colours)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + colour + noun + str(number) + special_char
    print("Your new password is:%s" % password)

    response = input("Would you like another password? y/n")
    if response == "n":
        break


