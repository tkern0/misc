from hashlib import md5
letters = "ckczppom"
i = 0
while 1 == 1:
    i += 1
    if str(md5((letters + str(i)).encode()).hexdigest())[:5] == "00000":
        print(letters + str(i), "encodes to", md5((letters + str(i)).encode()).hexdigest())
        break
i = 0
while 1 == 1:
    i += 1
    if str(md5((letters + str(i)).encode()).hexdigest())[:6] == "000000":
        print(letters + str(i), "encodes to", md5((letters + str(i)).encode()).hexdigest())
        break
