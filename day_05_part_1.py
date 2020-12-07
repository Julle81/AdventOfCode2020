import math

with open('day_05_input.txt') as f:
    boarding_passes = [line.rstrip() for line in f]

i = 0
highest_seat_id = 0

while i < len(boarding_passes):
    
    pass_index = 0
    upperRowLimit = 127
    lowerRowLimit = 0
    upperColumnLimit = 7
    lowerColumnLimit = 0
    row = 0
    column = 0
    boarding_pass = boarding_passes[i]

    while pass_index < len(boarding_pass):

        seat_letter = boarding_pass[pass_index]
        if( seat_letter == 'F'):
            upperRowLimit = lowerRowLimit + math.floor((upperRowLimit - lowerRowLimit) / 2)
            lowerRowLimit = lowerRowLimit
            row = upperRowLimit
        elif( seat_letter == 'B'):
            lowerRowLimit = lowerRowLimit + math.ceil((upperRowLimit - lowerRowLimit) / 2)
            upperRowLimit = upperRowLimit
            row = lowerRowLimit
        elif( seat_letter == 'R'):
            lowerColumnLimit = lowerColumnLimit + math.ceil((upperColumnLimit - lowerColumnLimit) / 2)
            upperColumnLimit = upperColumnLimit
            column = lowerColumnLimit
        elif( seat_letter == 'L'):
            upperColumnLimit = lowerColumnLimit + math.floor((upperColumnLimit - lowerColumnLimit) / 2)
            lowerColumnLimit = lowerColumnLimit
            column = upperColumnLimit

        pass_index += 1

    seat_id = row * 8 + column

    if( seat_id > highest_seat_id ):
        highest_seat_id = seat_id

    i += 1


print(highest_seat_id)