import png

def safe(list):
    new_list = []
    for i in list:
        new_list.append(int(i % 256))
    return new_list

# w, h = 256, 256
# pixels = []
# for y in range(w):
#    current_row = []
#    for x in range(h):
#        current_row.append(safe([x^y, x^y, x^y]))
#        pixels.append(current_row)
# png.from_array(pixels, "RGB").save("output.png")

pixels = []
y = 0
out = png.Reader('1.png').asRGBA()
w, h = out[0], out[1]
for row in out[2]:
    current_row = []
    for i in range(0, len(row), 4):
        x = int(i/4)
        r, b, g = row[i], row[i+1], row[i+2]
        current_row.append(safe([int((x+y)/16)^r, int((x+y)/16)^b, int((x+y)/16)^g]))
    pixels.append(current_row)
    y += 1
    print(y)

png.from_array(pixels, "RGB").save("1_out.png")
