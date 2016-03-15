num = "3113322113"
combo = 1
newNum = ""
for repeat in range(40):
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            combo += 1
        else:
            newNum += (str(combo) + num[i])
            combo = 1
    newNum += (str(combo) + num[-1])
    combo = 1
    num = newNum
    print(str(int(100 * ((repeat + 1) / 40))) + "%")
print("The length of the string is", len(num))
# From goo.gl/dSJcrk:
#from itertools import groupby
#
#def look_and_say(input_string, num_iterations):
#    for i in xrange(num_iterations):
#        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
#    return input_string
