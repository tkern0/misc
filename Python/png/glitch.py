import math as maths
import png
import random

PHI = (1+maths.sqrt(5))/2

def xor_list(list, value):
    return [[(i^value)%256 for i in j] for j in list]

def shift_list(list, amount):
    amount = amount % len(list)
    return list[amount:] + list[:amount]

pixels = []
y = 0
out = png.Reader("glitch_in.png").asRGBA()
w, h = out[0], out[1]
for row in out[2]:
    current_row = []
    for i in range(0, len(row), 4):
        x = int(i/4)
        r, g, b = row[i], row[i+1], row[i+2]
        current_row.append([r, g, b])
    current_row = xor_list(current_row, int((16*y/h)**2))
    current_row = shift_list(current_row, int(PHI * maths.sin(16*y/h) * (y-(h/2))**2/h - (PHI-1)*w))
    pixels.append(current_row)
    y += 1
    print(y)

# pixels = shift_list(pixels, -int((PHI-1)*h))
png.from_array(pixels, "RGB").save("glitch_out.png")