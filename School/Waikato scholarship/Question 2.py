# Tested using Python 3.2.1, but any 3.x.x version should work too

import re

# It's faster to compile regex if you're going to use it more than once
# It also makes the lines cleaner later, so it's a win-win
R_INPUT = re.compile(r"([TCPD])([AB])", flags=re.IGNORECASE)
MODERN_POINTS =   {"T": 5, "C": 2, "P": 3, "D": 3}
ORIGINAL_POINTS = {"T": 0, "C": 1, "P": 1, "D": 1}

# This gets used twice so it's better as a fucntion
def get_winner(A, B):
    if A > B:
        return "A Wins"
    elif A < B:
        return "B Wins"
    else:
        return "Tie"

events_A = {"T": 0, "C": 0, "P": 0, "D": 0}
events_B = {"T": 0, "C": 0, "P": 0, "D": 0}
last_event = ""

print("Welcome to Rugby scoring")
print("")
print("Instructions:")
print("- Refer to your teams as A and B")
print("- Events are T(ry), C(onversion), P(enalty), or D(ropped goal)")
print("- Enter events as \"Event Team\": eg: TA for a try by team A")
print("- Enter X at the end of the game")
print("")

while True:
    # Need to check input first
    while True:
        event = input("Enter Event: ")
        e_match = re.match(R_INPUT, event)
        # Conversion rules
        # Incorrect format (e.g. "C, Team A") should overwrite this, so this
        #  checks exact values
        if ((event == "CA" and not last_event == "TA") or
            (event == "CB" and not last_event == "TB")):
            print("A Conversion can only occur immediately after a Try")
            continue # Causes the current loop to instantly restart
        # If there is no match e_match is 'None' which evaluates to false
        if event.upper() == "X" or (e_match and len(event) == 2):
            # This only breaks out of one loop, so we'll need to check for the
            #  end of the game again
            break
        print("Could not recognise input, please try again")
    if event.upper() == "X":
        break
    # Group 2 is team
    # If the user entered lowercase there is still a match, but the group
    #  returns their lowercase value, so we need to convert it
    if e_match.group(2).upper() == "A":
        # Group 1 is the event type
        events_A[e_match.group(1).upper()] += 1
    elif e_match.group(2).upper() == "B":
        events_B[e_match.group(1).upper()] += 1
    else:
        # This bit should never run, here just in case
        print("Unknown team, something has gone horribly wrong")
        # Re-calls the last exception
        # Funnily enough if there hasn't been an exception yet it creates an
        #  exception for not being able to raise one
        # In any case the program crashes
        raise

# Game's over, time to work out the scores
# Using list comprehension here, even though it's probably faster to add
#  everything manually, it just looks nicer
score_A = sum([events_A[event]*MODERN_POINTS[event] for event in "TCPD"])
score_B = sum([events_B[event]*MODERN_POINTS[event] for event in "TCPD"])
winner = get_winner(score_A, score_B)

print("")
print("Modern Result: " + winner)

score_A = sum([events_A[event]*ORIGINAL_POINTS[event] for event in "TCPD"])
score_B = sum([events_B[event]*ORIGINAL_POINTS[event] for event in "TCPD"])
winner = get_winner(score_A, score_B)
# Tiebreaker is unconverted Tries, Tries - Conversions
if winner == "Tie":
    winner = get_winner(events_A["T"] - events_A["C"],
                        events_B["T"] - events_B["C"])

print("Original Result: " + winner)