# Made for a L1 programming assignment, at a time when I could easily pass a L3
# Comments starting with a dash were handed in, others were added later

import random
# -Gets the user's name, allowing only letters, spaces and hyphens
# why was this a requirement, it's so arbitrary
# there's also no reason the get the user's name at all
# user friendlyness != being friendly to the user
letters = "qwertyuiopasdfghjklzxcvbnm- "
while True:
    try:
        name = input("What is your name? ")
        for i in name:
            if i.lower() not in letters: raise ValueError
    except ValueError: print("Please use only letters in your name")
    else: break
# -The game
while True:
    secret_num, num_guessed = random.randint(1, 7), 0
    # -While the number is not guessed
    # even people who don't program can get that, why did I need to comment everything
    while not secret_num == num_guessed:
        while True:
            try:
                num_guessed = int(input("Try guess the number: "))
                if not num_guessed in range(1, 8): raise ValueError # If not 1 2 3 4 5 6 or 7
            except ValueError: print("Please enter a number between between 1 and 7")
            else: break
        if num_guessed > secret_num: print(str(num_guessed) + "? Too high!")
        elif num_guessed < secret_num: print(str(num_guessed) + "? Too low!")
    # you don't need this entire sentence, "Correct!" will do
    # but it was in the requirements
    print("Well done, {}! You guessed the secret number! It was {}!".format(name, secret_num))
    while True: # -Work out if to continue
        try:
            cont = input("Do you want to continue? [Y/N] ").lower()
            if not cont in ("y", "n"): raise ValueError
        except ValueError: print("Please enter either Y or N")
        else: break
    if cont == "n": break
print("Have a nice day! Thanks for playing!")