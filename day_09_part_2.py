with open('day_09_input.txt') as f:
    numbers = [line.rstrip() for line in f]

index = 0
checkable_numbers = []
while index < 25:
    checkable_numbers.append(numbers[index])
    index += 1

checksum = 0
i = 25

while i < len(numbers):
    check = numbers[i]
    
    check_index = 0
    while check_index < len(checkable_numbers):
        sum_check_index = check_index + 1
        while sum_check_index < len(checkable_numbers):
            sum_of_checks = int(checkable_numbers[check_index]) + int(checkable_numbers[sum_check_index])
            checksum = int(check)
            if(checksum == sum_of_checks):
                break
            sum_check_index += 1

        if sum_check_index < len(checkable_numbers):
            break 
        check_index += 1

    if sum_check_index == len(checkable_numbers) and check_index == len(checkable_numbers):
        break

    checkable_numbers.remove(checkable_numbers[0])
    checkable_numbers.append(check)

    i += 1

i = 0

while i < len(numbers):
    
    sum_of_cont = 0
    check_index = i
    lowest = int(numbers[i])
    highest = 0

    print("Round: " + str(i) )

    while check_index < len(numbers) and sum_of_cont < checksum:
        number = int(numbers[check_index])
        sum_of_cont += number
        if lowest > number:
            lowest = number 
        if highest < number:
            highest = number 

        check_index += 1

    if checksum == sum_of_cont:
        break
    
    i += 1

producing = lowest + highest
print(producing)