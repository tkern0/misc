import png
import random
import sys

def clamp(n, min_val=0, max_val=255): return max(min(n, max_val), min_val)
def random_chance(chance): return random.random() <= chance

def neighbours(coords):
    x, y = coords[0], coords[1]
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

def nearby_circle(coords, radius):
    out = []
    for x in range(coords[0] - radius, coords[0] + radius + 1):
        for y in range(coords[1] - radius, coords[1] + radius + 1):
            if ((x - coords[0])**2 + (y - coords[1])**2)**0.5 <= radius:
                out.append((x, y))
    return tuple(out)

def av_colour(list):
    l = len(list)
    r = sum([i[0] for i in list])/l
    g = sum([i[1] for i in list])/l
    b = sum([i[2] for i in list])/l
    return (r, g, b)

def random_colour(min=(0,0,0), max=(255,255,255)):
    r = random.randrange(min[0], max[0] + 1)
    g = random.randrange(min[1], max[1] + 1)
    b = random.randrange(min[2], max[2] + 1)
    return (r, g, b)

def gauss_colour(colour, sigma=16):
    r = int(random.gauss(colour[0], sigma))
    g = int(random.gauss(colour[1], sigma))
    b = int(random.gauss(colour[2], sigma))
    if 0 >= r >= 255: r = colour[0] + (colour[0] - r)
    if 0 >= g >= 255: g = colour[1] + (colour[1] - g)
    if 0 >= b >= 255: b = colour[2] + (colour[2] - b)
    return (r, g, b)

def set_pixel(coords, colour):
    global image
    global check_pixels
    if 0 > coords[0] >= WIDTH or 0 > coords[1] >= HEIGHT:
        return
    check_pixels.discard(coords)
    if coords not in image:
        image[coords] = colour
        for i in neighbours(coords):
            if 0 <= i[0] < WIDTH and 0 <= i[1] < HEIGHT:
                check_pixels.add(i)

def save_image(path):
    image_list = []
    for y in range(HEIGHT):
        current_row = []
        for x in range(WIDTH):
            if (x, y) in image:
                colour = image[(x, y)]
                current_row += [clamp(colour[0]), clamp(colour[1]), clamp(colour[2]), 255]
            else:
                current_row += [0, 0, 0, 0]
        image_list.append(current_row)
    png.from_array(image_list, "RGBA").save(path)

WIDTH  = W = 512
HEIGHT = H = 512

VENUS = lambda: random_colour((180, 150, 80), (255, 220, 180))
JUPITER = lambda: random_colour((180, 160, 120), (220, 220, 180))
SATURN = lambda: random_colour((200, 150, 80), (255, 255, 180))
ACCENT_1 = lambda: random.choice(((245, 245, 220), (139, 62, 47), (139, 129, 76), (139, 105, 105)))

URANUS = lambda: random_colour((50, 120, 200), (180, 220, 255))
NEPTUNE = lambda: random_colour((30, 30, 150), (80, 120, 255))
ACCENT_2 = lambda: random.choice(((245, 245, 220), (83, 134, 139), (139, 85, 98), (69, 139, 446)))

SHOW_ALL = False

if len(sys.argv) > 1: random.seed(sys.argv[1])

image = {}
check_pixels = set()
main_gradient = random.uniform(0, 5.0)
if random_chance(0.5):
    main_gradient = 1/main_gradient
if main_gradient > 0:
    min_start = int(WIDTH * main_gradient * -1.1)
    max_start = HEIGHT
elif main_gradient < 0:
    min_start = 0
    max_start = int((HEIGHT - (WIDTH * main_gradient)) * 1.1)
elif main_gradient == 0:
    min_start = 0
    max_start = HEIGHT

for _ in range(5):
    y_start = random.randrange(min_start, max_start)
    gradient = random.gauss(main_gradient, 0.05)
    colour = ACCENT_2()
    for y in range(y_start - 1, y_start + 2):
        for x in range(WIDTH):
            set_pixel((x, int(y)), gauss_colour(colour))
            y += gradient

for _ in range(int((WIDTH + HEIGHT)/8)):
    y = random.randrange(min_start, max_start)
    gradient = random.gauss(main_gradient, 0.05)
    colour = NEPTUNE()
    for x in range(WIDTH):
        set_pixel((x, int(y)), gauss_colour(colour))
        y += gradient

print("Base lines generated")

if SHOW_ALL:
    save_image("planet_out/0000 lines.png")

iter = 1
while check_pixels:
    for coords in list(check_pixels):
        all_neighbours = []
        for i in nearby_circle(coords, 2):
            if i in image:
                all_neighbours.append(image[i])
        for i in all_neighbours:
            if len(all_neighbours) == 1:
                break
            if random_chance(0.25):
                all_neighbours.remove(i)
        colour = av_colour(all_neighbours)
        colour = gauss_colour(colour)
        set_pixel(coords, colour)
    if SHOW_ALL:
        save_image("planet_out/" + str(iter).zfill(4) + " iter.png")
        iter += 1

print("Whole image generated")

if SHOW_ALL:
    save_image("planet_out/" + str(iter + 1).zfill(4) + " final.png")
else:
    save_image("planet.png")

print("Image Saved")