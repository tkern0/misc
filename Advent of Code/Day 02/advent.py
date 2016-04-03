presents = open('Day 02\input.txt')
area = [0, 0, 0]
tarea, tribbon = 0, 0
for line in presents:
    l, w, h = line.split("x")
    l, w, h = int(l), int(w), int(h)
    area[0] = (l * w)
    area[1] = (l * h)
    area[2] = (w * h)
    for i in range(0,len(area)):
        tarea += 2 *area[i]
    tarea += min(area)

    tribbon += 2 * min([l + w, l + h, w + h])
    tribbon += l * w * h

print("The total amount of wrapping paper needed is", tarea, "square feet")
print("The total amount of ribbon needed is", tribbon, "feet")
