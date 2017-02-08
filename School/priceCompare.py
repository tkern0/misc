# Made for a L2 programming assignment, at a time when I could easily pass a L3
# Comments starting with a dash were handed in, others were added later

# -Prints out a dynamic ASCII table when given a dict as input
# -dict must be formatted as follows:
# -    {name:{columnName:value}}
# -All internal dicts must have the same columns
# -Can specify the order of columns if necessary
# -All items in dict (keys/values) must be strings
# I had some spare time, so I made it look nicer
# I actualy really like this function
def printTable(table, order = None):
    # -If 'order' not set
    if not order:
        # -Gets an arbitrary order
        order = list(table.values())[0].keys()
    # -Sets base max length of each column, based on name
    maxLen = {"Name": 4}
    for i in order:
        maxLen[i] = len(i)
    # -Finds true max length of each column
    for i in table:
        if len(i) > maxLen["Name"]:
            maxLen["Name"] = len(i)
        for j in table[i]:
            if len(table[i][j]) > maxLen[j]:
                maxLen[j] = len(table[i][j])
    # -Creates "+---+---+---+" or similar
    seperator = "+" + "-" * maxLen["Name"] + "+"
    for i in order:
        seperator += "-" * maxLen[i] + "+"
    # -Similar to how 'seperator' is created
    names = "|" + "Name" + " " * (maxLen["Name"] - 4) + "|"
    for i in order:
        names += i + " " * (maxLen[i] - len(i)) + "|"
    print(seperator)
    print(names)
    print(seperator)
    # -Similar to how 'seperator' is created, iterates through each row
    for i in table:
        currentRow = "|" + i + " " * (maxLen["Name"] - len(i)) + "|"
        for j in order:
            currentRow += table[i][j] + " " * (maxLen[j] - len(table[i][j])) + "|"
        print(currentRow)
    print(seperator)

# -Gets an float from the user
# -Can handle text inputs
def getFloat(prompt):
    while True:
        try:
            result = float(input(prompt))
        except ValueError:
            print("Please enter a number")
        else:
            break
    return result

# -Gets a Yes/No input from the user
# -Returns a boolean value
def getYN(prompt):
    while True:
        try:
            result = input(prompt + " [Y/N]")
            # -Acceptable values
            if not result in ("y", "n", "Y", "N", "yes", "no", "Yes", "No"):
                raise ValueError
        except ValueError:
            print("Please enter 'Y' or 'N")
        else:
            break
    return result in ("y", "Y", "yes", "Yes")

# -Gets the mean value of a list
def mean(list): return float(sum(list))/float(max(len(list), 1))

# -Gets user's name, because that's apparently a requirement despite it never being used again
# at least this one didn't have stupid requirements of what the user's name can be
while True:
    try:
        uName = input("What is your name? ")
        if len(uName) < 1:
            raise ValueError
    except ValueError:
        print("Please enter your name")
    else:
        break
print("Hello", uName)
# -Main loop
# -Gets a dict filled with info about all products that the user wants to compare
items = {}
while True:
    currentItem = {"Price": None, "Weight/Volume": None, "Unit Price": None}
    while True:
        try:
            currentName = input("What is the product you are comparing? ")
            if len(currentName) == 0:
                raise ValueError
            if currentName in items:
                if not getYN("'" + currentName + "' already exists. Do you want to overwrite it?"):
                    raise NameError
        except ValueError:
            print("Please enter a name")
        except NameError:
            pass
        else:
            break
    while not currentItem["Price"]:
        currentItem["Price"] = getFloat("How much does it cost? (dollars)")
        # -Warns if price > 100
        if currentItem["Price"] > 100:
            # -'"%.2f" % a' rounds 'a' to two decimals
            # -There might be a more readable method, in which case that should be replaced
            if getYN("Wow, that's expensive! Are you sure you want the price to be $" + "%.2f" % currentItem["Price"]):
                if currentItem["Price"] > 0:
                    break
                else:
                    print("Please enter a number greater than 0")
        else:
            if currentItem["Price"] > 0:
                break
            else:
                print("Please enter a number greater than 0")
    while not currentItem["Weight/Volume"]:
        currentItem["Weight/Volume"] = getFloat("What is the weight/volume? (g/ml)")
        # -Warns if weight/volume > 2000
        # at least I didn't need to get a new input if you weren't in range
        if currentItem["Weight/Volume"] > 2000:
            if getYN("Wow, that's a lot! Are you sure you want the weight/volume to be " + "%.2f" % currentItem["Weight/Volume"]):
                if currentItem["Weight/Volume"] > 0:
                    break
                else:
                    print("Please enter a number greater than 0")
        else:
            if currentItem["Weight/Volume"] > 0:
                break
            else:
                print("Please enter a number greater than 0")
    currentItem["Unit Price"] = currentItem["Price"] / currentItem["Weight/Volume"]
    print(currentName + ": $" + "%.2f" % currentItem["Price"] + ", " + "%.0f" % currentItem["Weight/Volume"])
    # -Converts floats to strings, rounding to either two or no decimals
    for k, v in currentItem.items():
       if v == int(v):
            currentItem[k] = str(int(v))
       else:
            currentItem[k] = str("%.2f" % v)
    if getYN("Are you happy with this item?"):
        items[currentName] = currentItem
    if len(items) > 0:
        if not getYN("Do you want to add more items?"):
            break

# -Creates a list of all unit price values
comparePPW = []
for i in items:
    comparePPW.append(float(items[i]["Unit Price"]))

printTable(items, ["Price", "Weight/Volume", "Unit Price"])
# -Other Stats:
print("The item(s) with the best value is/are:")
for i in items:
    if items[i]["Unit Price"] == "%.2f" % min(comparePPW):
        print(i)
print("Which have a unit price of $" + str("%.2f" % min(comparePPW)))
print("\nThe item(s) with the worst value is/are:")
for i in items:
    if items[i]["Unit Price"] == "%.2f" % max(comparePPW):
        print(i)
print("Which have a unit price of $" + "%.2f" % max(comparePPW))
print("\nThe average unit price is $" + "%.2f" % mean(comparePPW))
