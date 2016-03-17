def look_and_say(num, rl, repeat = 1):
    combo = 1
    for repeat in range(repeat):
        newNum = ""
        for i in range(len(num) - 1):
            if num[i] == num[i + 1]: combo += 1
            else:
                newNum += (str(combo) + num[i])
                combo = 1
        newNum += (str(combo) + num[-1])
        combo = 1
        num = newNum
    if rl: return len(num)
    else: return num
print("The length of the string in part 1 is", look_and_say("3113322113", True, 40))
print("The length of the string in part 2 is", look_and_say("3113322113", True, 50))
