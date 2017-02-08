import sys

class ProbablyString():
	def __init__(self, a):
		self.a = a

	def get_string(self):
		b = self.a
		return b

	def set_string(self, a):
		self.a = a


def char_to_num(a):
    if a == "a":
        return 1
    if a == "b":
        return 2
    if a == "c":
        return 3
    if a == "d":
        return 4
    if a == "e":
        return 5
    if a == "f":
        return 6
    if a == "g":
        return 7
    if a == "h":
        return 8
    if a == "i":
        return 9
    if a == "j":
        return 10
    if a == "k":
        return 11
    if a == "l":
        return 12
    if a == "m":
        return 13
    if a == "n":
        return 14
    if a == "o":
        return 15
    if a == "p":
        return 16
    if a == "q":
        return 17
    if a == "r":
        return 18
    if a == "s":
        return 19
    if a == "t":
        return 20
    if a == "u":
        return 21
    if a == "v":
        return 22
    if a == "w":
        return 23
    if a == "x":
        return 24
    if a == "y":
        return 25
    if a == "z":
        return 26
    if a == "!":
        return 27
    if a == "A":
        return 28
    if a == "B":
        return 29
    if a == "C":
        return 30
    if a == "D":
        return 31
    if a == "E":
        return 32
    if a == "F":
        return 33
    if a == "G":
        return 34
    if a == "H":
        return 35
    if a == "I":
        return 36
    if a == "J":
        return 37
    if a == "K":
        return 38
    if a == "L":
        return 39
    if a == "M":
        return 40
    if a == "N":
        return 41
    if a == "O":
        return 42
    if a == "P":
        return 43
    if a == "Q":
        return 44
    if a == "R":
        return 45
    if a == "S":
        return 46
    if a == "T":
        return 47
    if a == "U":
        return 48
    if a == "V":
        return 49
    if a == "W":
        return 50
    if a == "X":
        return 51
    if a == "Y":
        return 52
    if a == "Z":
        return 53
    if a == " ":
        return 54

def num_to_char(a):
    if a == 1:
        return "a"
    if a == 2:
        return "b"
    if a == 3:
        return "c"
    if a == 4:
        return "d"
    if a == 5:
        return "e"
    if a == 6:
        return "f"
    if a == 7:
        return "g"
    if a == 8:
        return "h"
    if a == 9:
        return "i"
    if a == 10:
        return "j"
    if a == 11:
        return "k"
    if a == 12:
        return "l"
    if a == 13:
        return "m"
    if a == 14:
        return "n"
    if a == 15:
        return "o"
    if a == 16:
        return "p"
    if a == 17:
        return "q"
    if a == 18:
        return "r"
    if a == 19:
        return "s"
    if a == 20:
        return "t"
    if a == 21:
        return "u"
    if a == 22:
        return "v"
    if a == 23:
        return "w"
    if a == 24:
        return "x"
    if a == 25:
        return "y"
    if a == 26:
        return "z"
    if a == 27:
        return "!"
    if a == 28:
        return "A"
    if a == 29:
        return "B"
    if a == 30:
        return "C"
    if a == 31:
        return "D"
    if a == 32:
        return "E"
    if a == 33:
        return "F"
    if a == 34:
        return "G"
    if a == 35:
        return "H"
    if a == 36:
        return "I"
    if a == 37:
        return "J"
    if a == 38:
        return "K"
    if a == 39:
        return "L"
    if a == 40:
        return "M"
    if a == 41:
        return "N"
    if a == 42:
        return "O"
    if a == 43:
        return "P"
    if a == 44:
        return "Q"
    if a == 45:
        return "R"
    if a == 46:
        return "S"
    if a == 47:
        return "T"
    if a == 48:
        return "U"
    if a == 49:
        return "V"
    if a == 50:
        return "W"
    if a == 51:
        return "X"
    if a == 52:
        return "Y"
    if a == 53:
        return "Z"
    if a == 54:
        return " "

def get_hello_world():
    a = ""
    while not a == "Hello World!":
        a = input("Type 'Hello World!'")
        if not a == "Hello World!":
            print("That was not the correct string")
    return a

def get_nums_from_string(a):
    b = []
    for i in a:
        c = char_to_num(i)
        b.append(c)
    return b

def get_string_from_nums(a):
    b = []
    for i in a:
        c = num_to_char(i)
        b.append(c)
    d = "".join(b)
    return d

def reverse_list(a):
    b = []
    c = len(a)
    for i in range(c):
        b.append(a[-i])
    return b

def string_from_list(a):
    b = "".join(a)
    return b

def list_from_string(a):
	b = list(a)
	return b

def print_list(a):
    for i in a:
        sys.stdout.write(i)

a = get_hello_world()
string = ProbablyString(a)
b = get_nums_from_string(string.get_string())
string.set_string(b)
c = reverse_list(string.get_string())
string.set_string(c)
d = get_string_from_nums(string.get_string())
string.set_string(d)
e = reverse_list(list(string.get_string()))
string.set_string(e)
f = string_from_list(string.get_string())
string.set_string(f)
g = list_from_string(string.get_string())
string.set_string(g)
print_list(string.get_string())