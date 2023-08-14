from PIL import Image, ImageDraw
import numpy as np


binary1 = '01101001011010'
binary2 = '10110110110110'

#binary1 = '1011'
#binary2 = '1110'

grid_size = 50

color1 = (214, 166, 190)
color2 = (162, 195, 200)

im = Image.new('RGB', ((len(binary1)+2)*grid_size, (len(binary2)+2)*grid_size), (255, 255, 255))
draw = ImageDraw.Draw(im)


def ar_c(bi):
    arr = []
    for j in bi:
        arr.append(int(j))

    return arr


def ar_m(k, m):
    arr = []
    for j in k:
        if j:
            arr.append(ar_c('10'*int(m/2)))
        else:
            arr.append(ar_c('01'*int(m/2)))

    return arr


def make(grid, orien):
    if orien == 'col':
        row_index = 0
        for i in grid:
            row_index += 1
            col_index = 0

            for j in i:
                col_index += 1
                if j:
                    draw.line(((grid_size*row_index, grid_size*col_index),
                               (grid_size*row_index, grid_size*(col_index+1))), fill=(0, 0, 0), width=5)
    else:
        col_index = 0
        for i in grid:
            col_index += 1
            row_index = 0

            for j in i:
                row_index += 1
                if j:
                    draw.line(((grid_size * row_index, grid_size * col_index),
                               (grid_size * (row_index + 1), grid_size * col_index)), fill=(0, 0, 0),
                              width=5)


def swapp(a, b):
    t = a
    a = b
    b = t


def color_one(bina, index1, color):
    #draw.rectangle(((grid_size, grid_size), (grid_size * 2, grid_size * 2)), fill=color1)
    index = 0
    for i in range(len(bina)):
        index += 1
        if int(bina[i]):
            if color == (214, 166, 190):
                color = (162, 195, 200)
            else:
                color = (214, 166, 190)

        draw.rectangle(((grid_size * index, grid_size * index1),
                        (grid_size * (index + 1), grid_size * (index1 + 1))), fill=color)


def color_m(grid, first_color, second_color, bina):
    for j in grid:
        for i in range(2, len(j), 2):
            color_one(j, i, first_color)
    for i in range(1, len(bina), 2):
        color_one(bina, i, first_color)


b = ar_m(ar_c(binary1), len(binary1))
color_m(np.transpose(b), (214, 166, 190), (162, 195, 200), binary1)
print(np.transpose(b))
make(b, 'col')
c = ar_m(ar_c(binary2), len(binary2))
make(c, 'row')
print('\n')
print(np.transpose(c))


im.show()
