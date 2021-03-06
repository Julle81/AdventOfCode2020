with open('day_08_input.txt') as f:
    operations = [line.rstrip() for line in f]

i = 0
executed_commands = []
accumulator = 0
while i < len(operations):

    if( i in executed_commands ):
        break    
    operation = operations[i]
    op = ""
    number = ""
    j= 0

    while j < 3:
        op += operation[j]
        j += 1

    sign = operation[4]
        
    j = 5
    while j < len(operation):
        number += operation[j]
        j += 1

    if( op == "nop"):
        executed_commands.append(i)
        i+=1
        continue
    elif( op == "acc"):
        executed_commands.append(i)
        i+=1
        if( sign == "+"):
            accumulator += int(number)
        elif( sign == "-"):
            accumulator -= int(number)
        continue
    elif( op == "jmp"):
        executed_commands.append(i)
        if( sign == "+"):
            i += int(number)
        elif( sign == "-"):
            i -= int(number)
        continue

print(accumulator)
