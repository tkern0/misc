import colorsys as coloursys
import math as maths
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

def gauss_colour(colour, sigma):
    r = random.gauss(colour[0], sigma)
    g = random.gauss(colour[1], sigma)
    b = random.gauss(colour[2], sigma)
    return (r, g, b)

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

def set_pixel(coords, colour):
    global image
    if 0 <= coords[0] < WIDTH or 0 <= coords[1] < HEIGHT:
        image[coords] = colour

def rand_HLS(h_mu, h_sigma, l_mu, l_sigma, s_mu, s_sigma):
    h = random.gauss(h_mu, h_sigma)
    if h < 0: h += 1
    if h > 1: h -= 1
    l = clamp(random.gauss(l_mu, l_sigma), 0, 1)
    s = clamp(random.gauss(s_mu, s_sigma), 0, 1)
    r, g, b = coloursys.hls_to_rgb(h, l, s)
    r *= 255
    g *= 255
    b *= 255
    return (r, g, b)

WIDTH  = W = 512
HEIGHT = H = 512
SHOW_ALL = False
if len(sys.argv) > 1: random.seed("".join(sys.argv[1:]))
image = {}

sk_colour = rand_HLS(210/360, 20/360, 0.3, 0.1, 0.3, 0.1)
for x in range(0, W):
    for y in range(0, H):
        set_pixel((x, y), gauss_colour(sk_colour, 1))

# Stars
st_num = W*H*0.0005
for pixel in random.sample(range(W*H), k=clamp(int(abs(random.gauss(st_num, st_num))), 0, W*H*.1)):
    x = pixel % W
    y = int(pixel/W)
    st_colour = gauss_colour((250, 250, 250), 16)
    set_pixel((x, y), gauss_colour(st_colour, 1))
    for i in neighbours((x, y)):
        set_pixel(i, gauss_colour(st_colour, 1))

# Moon
m_x = random.randint(-50, W + 50)
m_y = clamp(int(random.gauss(75, 10)), 50, 150)
m_radius = abs(int(random.gauss(75, 10)/2))
m_grey = clamp(random.gauss(220, 20))
for i in nearby_circle((m_x, m_y), m_radius):
    m_random_grey = clamp(random.gauss(m_grey, 5))
    m_colour = (m_random_grey, m_random_grey, m_random_grey)
    set_pixel(i, m_colour)

# All the buildings (5 layers)
for _ in range(5):
    b_x = random.randint(-90, 0)
    # Each layer is filled completly horizontally
    while b_x < W:
        b_colour = rand_HLS(30/360, 15/360, 0.1, 0.1, 0.3, 0.2)
        b_width = clamp(int(random.gauss(120, 20)), 50, 200)
        b_height = clamp(int(random.gauss(300, 75)), 50, 400)
        for x in range(b_x, b_x + b_width):
            for y in range(H - b_height, H):
                set_pixel((x, y), gauss_colour(b_colour, 1))
        # Windows
        # Turns out this is complex
        bw_base_colour = rand_HLS(210/360, 10/360, 0.2, 0.1, 0.2, 0.1)
        bw_horiz_num = clamp(int(random.gauss(b_width/20, 2)), 2, 20)
        bw_vert_num = clamp(int(random.gauss(b_height/20, 2)), 2, 20)
        bw_width = int(b_width / (bw_horiz_num + 1))
        bw_height = int(b_height / (bw_vert_num + 3))
        bw_horiz_offset = clamp(int((b_width - bw_width*bw_horiz_num) / (bw_horiz_num + 1)), 2, 10)
        bw_vert_offset = clamp(int((b_height - bw_height*bw_vert_num) / (bw_vert_num + 1)), 2, 10)
        
        for bw_x in range(b_x + bw_horiz_offset + 2, b_x + b_width - bw_width, bw_width + bw_horiz_offset):
            for bw_y in range(H - b_height + bw_vert_offset + 2, H, bw_height + bw_vert_offset):
                bw_colour = gauss_colour(bw_base_colour, 4)
                for x in range(bw_x, bw_x + bw_width):
                    for y in range(bw_y, bw_y + bw_height):
                        set_pixel((x, y), bw_colour)
        b_x += b_width

# Highway
h_height = clamp(int(random.gauss(70, 10)), 20, 100)
h_horiz_offset = clamp(int(random.gauss(0, W/2)), -W, W)
h_grey = clamp(random.gauss(24, 8))
h_colour = (h_grey, h_grey, h_grey)
for x in range(W):
    for y in range(H - h_height - 5, H):
        # Essentially just transforming + inverting the inequality y > +/- tan(x)
        if not ((y+h_height-H)*10/h_height > maths.tan((x-W/2-h_horiz_offset)*(2*maths.pi)/W)
               and (y+h_height-H)*10/h_height > -maths.tan((x-W/2-h_horiz_offset)*(2*maths.pi)/W)):
            set_pixel((x, y), gauss_colour(h_colour, 1))

save_image("city.png")