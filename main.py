'''
this program just create the pattern
change the binary and you'll get a plain image(B&W) of the pattern

'''
from PIL import Image, ImageDraw


binary1 = '01101001011010'
binary2 = '10110110110110'

# binary1 = '1011'
# binary2 = '1110'

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


b = ar_m(ar_c(binary1), len(binary1))
# for i in b:
#     print(i)v
make(b, 'col')
c = ar_m(ar_c(binary2), len(binary2))
make(c, 'row')


im.show()
