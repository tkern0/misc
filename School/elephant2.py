animals = {"Elephant":{"Legs":4, "Height":4.5, "Tail":True}, "Chicken":{"Legs":2, "Height":0.1, "Tail":True}, "Spider":{"Legs":8, "Height":0.02, "Tail": False}, "Human":{"Legs":2, "Height":1.8, "Tail": False}}
for i in animals:
    print(i + ":")
    for j in animals[i]: print(j + ":" + str(animals[i][j]))