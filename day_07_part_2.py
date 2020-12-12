with open('day_07_input.txt') as f:
    colour_rules = [line.rstrip() for line in f]

i = 0
colours_can_contain = []
temp_colours = []
amount = 0

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
        while colour_rule[index] != " ":
            string_amount += colour_rule[index]
            index += 1

        amount += int(string_amount)

        temp_colours.append(colour_not_this)
    
    i += 1

while True:
    colours_to_check = []
    j = 0
    while j < len(temp_colours):
        rule_index = 0
        colour_to_find = temp_colours[j];
        while rule_index < len(colour_rules):
            colour_rule = colour_rules[rule_index]
            colour = ""
                           
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
            if( colour_rule.find(colour_to_find) != -1):
                if colour not in colours_can_contain:
                    colours_can_contain.append(colour)
                colours_to_check.append(colour)
            
            rule_index += 1
        j += 1

    temp_colours = colours_to_check

    if not temp_colours:
        break


print(len(colours_can_contain))
