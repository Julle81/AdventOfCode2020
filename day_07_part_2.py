import re

with open('day_07_input.txt') as f:
    colour_rules = [line.rstrip() for line in f]

i = 0
colours_can_contain = []
temp_colours = []
amount_of_bags = 0

while i < len(colour_rules):
    colour_rule = colour_rules[i]
    colour = ""
    string_amount = ""
    
    pass_through = 0
    char_index = 0
    while pass_through < 2:
        
        while colour_rule[char_index] != " ":
            colour += colour_rule[char_index]
            char_index += 1

        if( pass_through == 0):
            colour += " "

        char_index += 1
        pass_through +=1

    colour_rule = colour_rule[len(colour) + 1:]
    if( colour == "shiny gold" ):
        index = colour_rule.find("contain") + len("contain") + 1

        no_of_bags = [int(s) for s in re.findall(r'\b\d+\b', colour_rule)]
        bag_index = 0
        while bag_index < len(no_of_bags):
            amount_of_bags += no_of_bags[bag_index]
            bag_index += 1
        next_colours_to_check = [s for s in re.findall(r'\b[0-9] * bags+\b', colour_rule)]

        temp_colours.append(next_colours_to_check)
    
    i += 1


print(temp_colours)
