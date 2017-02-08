p = input("Password: ")
a = open("pass.txt")
if sha512(str.encode(p)).hexdigest() == a.read():
    print("correct")
else:
    print("wrong")