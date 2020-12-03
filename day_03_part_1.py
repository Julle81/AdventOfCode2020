with open('day_03_input.txt') as f:
    slopes = [line.rstrip() for line in f]

i = 1
going_right = 0
no_of_trees = 0

while i < len(slopes):

    slope_line = slopes[i];
    going_right += 3

    while len(slope_line) - 1 < going_right:
            slope_line += slopes[i]    

    if( slope_line[going_right] == '#'):
        no_of_trees +=1
    i+=1


print(no_of_trees)