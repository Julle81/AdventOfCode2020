with open('day_03_input.txt') as f:
    slopes = [line.rstrip() for line in f]

going_right = 0

iterations = 0

multiple_of_trees = 1

def go_right(i):   
    switcher={
        0:1,
        1:3,
        2:5,
        3:7,
        4:1
    }
    return switcher.get(i)


while iterations < 5:

    i = 1
    no_of_trees = 0

    how_many_right = go_right(iterations)

    how_many_down = 1
    if( iterations == 4 ):
        i = 2
        how_many_down = 2

    going_right = 0
    
    while i < len(slopes):

        slope_line = slopes[i];
        going_right += how_many_right

        while len(slope_line) - 1 < going_right:
                slope_line += slopes[i]    

#        index_string = "index taken from: {}"
#        slope_info_string = slope_line + " and len is: {}"
#        print(index_string.format(going_right))
#        print(slope_info_string.format(len(slope_line)))
#        print(slope_line[going_right])

        if( slope_line[going_right] == '#'):
            no_of_trees += 1
        i += how_many_down


    iterations += 1
    multiple_of_trees *= no_of_trees
    print(no_of_trees)
 
print(multiple_of_trees)
