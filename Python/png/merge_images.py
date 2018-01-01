import png

def safe(list):
    new_list = []
    for i in list:
        new_list.append(int(i % 256))
    return new_list



full_image = []
in1 = png.Reader("1.png").asRGBA()
in2 = png.Reader("2.png").asRGBA()
w, h = in1[0], in1[1]

WEIGHT = 1.0
AV_TOTAL = WEIGHT + 1

if not w == in2[0] and not h == in2[1]:
    raise ValueError

for row in in1[2]:
    current_row = []
    for i in range(0, len(row), 4):
        r = row[i] * WEIGHT
        g = row[i + 1] * WEIGHT
        b = row[i + 2] * WEIGHT
        current_row.append([r, g, b])
    full_image.append(current_row)

row_num = 0
for row in in2[2]:
    for i in range(0, len(row), 4):
        full_image[row_num][int(i/4)][0] += row[i]
        full_image[row_num][int(i/4)][1] += row[i + 1]
        full_image[row_num][int(i/4)][2] += row[i + 2]
    row_num += 1

new_image = []
for row in full_image:
    current_row = []
    for pixel in row:
        current_pixel = []
        for colour in pixel:
            current_pixel.append(colour/AV_TOTAL)
        current_row.append(safe(current_pixel))
    new_image.append(current_row)


png.from_array(new_image, "RGB").save("out.png")
