'''
here i am trying to enhance test2.py
i will perform color break
then adding them, to get, maybe desired output

before trying barriers came
how would you break these two colors into something that on mixing they give the desired output

then after some critical thingking
i found that there are left over spots
meaning on over-laping those two col and row photos together we get some places that have the same color
so even if we did overcome the first barrier we would get 3 diffrent spots for the colors
so instead of adding those two color vectors together
we could just make use of 3 diffrent colors from single side only

col   row     color
0      0        c1
0      1        c2
1      0        c2
1      1        c3

not desired output
so after some more thinking
there are no combinations where they are same in the grid

'''


from PIL import Image, ImageDraw

'''
binary1 = '01101001011010'
#binary2 = '10110110110110'
binary2 = binary1
'''

binary1 = '1011'
binary2 = '1110'


color1 = (214, 166, 190) # (234, 186, 210)    (194, 146, 170)
color2 = (162, 195, 200) #  (182, 215, 220)     (142, 175, 180)
color3 = (192, 200, 162)
# color4 = (200, 162, 162)

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
draw.rectangle((x, y, x+grid_size, y+grid_size), fill=(0, 192, 192))

draw.rectangle((x, y, x+grid_size, y+grid_size), fill=(0, 192, 192))


def color_m(grid, other, orien):
    if orien == 'col':
        row_index = 0
        for i in grid:
            col_index = 0
            for j in i:

                if j == 1 and other[col_index][row_index] == 1:
                    draw.rectangle(((grid_size*row_index, grid_size*col_index),
                                    (grid_size*(row_index+1), grid_size*(col_index+1))), fill=color3)
                elif j == 0 and other[row_index][col_index] == 0:
                    draw.rectangle(((grid_size*row_index, grid_size*col_index),
                                    (grid_size*(row_index+1), grid_size*(col_index+1))), fill=color1)
                else:
                    draw.rectangle(((grid_size*row_index, grid_size*col_index),
                                    (grid_size*(row_index+1), grid_size*(col_index+1))), fill=color2)
                col_index += 1
            row_index += 1

    else:
        col_index = 0
        for i in grid:
            col_index += 1
            row_index = 0

            for j in i:
                row_index += 1
                if j == 0 and other[row_index][col_index] == 0:
                    draw.rectangle(((grid_size * row_index, grid_size * col_index),
                                    (grid_size * (row_index + 1), grid_size * (col_index + 1))), fill=color3)
                else:
                    draw.rectangle(((grid_size * row_index, grid_size * col_index),
                                    (grid_size * (row_index + 1), grid_size * (col_index + 1))), fill=color1)



b = ar_m(ar_c(binary1), len(binary1))
c = ar_m(ar_c(binary2), len(binary2))

for i in b:
    print(i)
print("88888888888888888888888888")
for i in c:
    print(i)

print(c[0][1])
color_m(b, c, "col")
# for i in b:
#     print(i)
#make(b, 'col')

#make(c, 'row')


im.show()
