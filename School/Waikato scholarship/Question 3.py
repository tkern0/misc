# Tested using Python 3.2.1, but any 3.x.x version should work too

# This may need to be updated for other PCs
STV_DIR = "E:\\STV.txt"
TOTAL_VOTES = 1000

# Finds the key with the lowest value in a dict
def lowest_dict(d):
    # There was a much nicer way to do this that I've forgotten
    l_val = TOTAL_VOTES
    l_key = None
    for i in d:
        if d[i] < l_val:
            l_val = d[i]
            l_key = i
    return l_key

# First create a list of all prefrences
# We don't just take a list of all voters because in most cases there will be
#  far more voters than possible prefrence orders, so after initall processing
#  this method is faster
votes = {}
with open(STV_DIR) as file:
    for line in file:
        # Unfortuantly we can't use a list as a key in a dictionary,
        #  so we have to convert to a tuple
        # This means we'll have to create new dictionaries as candidates are
        #  eliminated, through it should take the same amount of time
        pref = tuple(line.strip().split(" "))
        # Because not all possible prefrence orders may exist, we create them
        #  when a new one is read
        if pref in votes:
            votes[pref] += 1
        else:
            votes[pref] = 1
# When we leave the 'with' function the file automatically is closed, to save a
#  bit more memory

while True:
    current_pref = {}
    for i in votes:
        # Not all candidates are necessarly selected, so again we create them as
        #  we find new ones
        if i[0] in current_pref:
            current_pref[i[0]] += votes[i]
        else:
            current_pref[i[0]] = votes[i]

    print("Current preferences:")
    # We sort the dictinary keys to get a nicer output
    # In this case we get '1,2,3,4,5' rather than something like '1,3,2,5,4'
    for i in sorted(current_pref.keys()):
        print("Candidate {}: {} votes".format(i, current_pref[i]))
    print("")

    l_candidate = lowest_dict(current_pref)
    # If there are only two candidates, the winner is the one not in "l_candidate"
    if len(current_pref) == 2:
        winner = list(current_pref.keys())
        winner.remove(l_candidate)
        winner = winner[0]
        break
    # If there was not a winner we need to eliminate a candidate
    new_votes = {}
    for i in votes:
        pref = list(i)
        if l_candidate in pref:
            pref.remove(l_candidate)
        else:
            # If they don't have the lowest candidate they must have at least
            #   one "0"
            # To makes sure all tuples are the same length we remove one
            # We could add a "0" to the tuples we remove the lowest candidate
            #  from, but that's just a waste of memory
            pref.remove("0")
        # If 'pref' is just zeros
        if pref.count("0") == len(pref):
            continue # Instantly restart the loop, skipping the rest
        pref = tuple(pref)
        # Removing the lowest candidate may have made some prefences equal
        if pref in new_votes:
            new_votes[pref] += votes[i]
        else:
            new_votes[pref] = votes[i]
    votes = new_votes
    # Save a bit more memory
    new_votes = None
    print("Candidate {} eliminated".format(l_candidate))
    print("")

print("Candidate {} is elected".format(winner))