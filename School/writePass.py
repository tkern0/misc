from hashlib import sha512
p = input("Password: ")
a = open("pass.txt", "w")
a.write(sha512(str.encode(p)).hexdigest())
a.close()