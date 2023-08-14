'''
adding color can be tricky
either do it manually with paint after closing all the pattern
or use your brain
'''

from PIL import Image, ImageDraw


binary1 = '01101001011010'
binary2 = '10110110110110'

color1 = (214, 166, 190)
color2 = (162, 195, 200)

grid_size = 50

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


x = 200
y = 100
#draw.rectangle((x, y, x+grid_size, y+grid_size), fill=(0, 192, 192))

#draw.rectangle((x, y, x+grid_size, y+grid_size), fill=(0, 192, 192))


def color_m(grid, orien):
    if orien == 'col':
        row_index = 0
        for i in grid:
            row_index += 1
            col_index = 0

            for j in i:
                col_index += 1
                if j:
                    draw.rectangle(((grid_size*row_index, grid_size*col_index),
                                    (grid_size*(row_index+1), grid_size*(col_index+1))), fill=color1)
                else:
                    draw.rectangle(((grid_size*row_index, grid_size*col_index),
                                    (grid_size*(row_index+1), grid_size*(col_index+1))), fill=color2)

    else:
        pass


b = ar_m(ar_c(binary1), len(binary1))
color_m(b, "col")
# for i in b:
#     print(i)v
make(b, 'col')
c = ar_m(ar_c(binary2), len(binary2))
make(c, 'row')


im.show()
