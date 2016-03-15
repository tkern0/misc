dirs = open('input.txt').read()
floor = 0
basement = 0
for i in range(0,len(dirs)):
    if dirs[i]=='(':
        floor+=1
    elif dirs[i]==')':
        floor-=1
    else:
        print("Incorrect Character")
        break
    if floor==-1 and basement==0:
        print("Santa first enters the basement on position", i+1)
        basement=1
print("Santa is on floor", floor)
