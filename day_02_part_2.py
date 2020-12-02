with open('day_02_input.txt') as f:
    passwords = [line.rstrip() for line in f]


valid_passwords = 0
pass_through = 0

while pass_through < len(passwords):
    whole_string = passwords[pass_through];
    
    password_valid = True
    
    index = whole_string.find(':')

    i = 0;
    first_number_as_string = whole_string[i]
    i += 1 

    while True:

        if( whole_string[i] != '-'):
            first_number_as_string += whole_string[i]
            i += 1
        else: 
            i += 1
            break


    second_number_as_string = whole_string[i]
    i += 1 

    while True:

        if( whole_string[i] != ' '):
            second_number_as_string += whole_string[i]
            i += 1 
        else:
            i += 1 
            break

    first_number = int(first_number_as_string) - 1 #Index is one smaller then the position
    second_number = int(second_number_as_string) - 1 #Index is one smaller then the position
    
    letter = whole_string[i]
    i += 2
    amount = len(whole_string) - (i + 1)
    password = whole_string[-amount:]
    
    if( password[first_number] == letter and password[second_number] == letter):
        password_valid = False
    elif( password[first_number] != letter and password[second_number] != letter):
        password_valid = False

    if( password_valid ):
        valid_passwords += 1

    pass_through += 1

print(valid_passwords)