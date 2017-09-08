def bigNum(number):
  MAGIC = {"0":33282801630,
           "1":13907313471,
           "2":33069516351,
           "3":66626269438,
           "4":6615084994,
           "5":67124601020,
           "6":32764995740,
           "7":67697689356,
           "8":33075969246,
           "9":15322116190}
  for digit in str(number):
    for i in range(1,7): print(str(bin(MAGIC[digit]))[2:].zfill(36)[(i-1)*6:i*6].replace("0"," ").replace("1", "#"))
    print("")
    
bigNum(1234567890)