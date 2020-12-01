with open('input.txt') as f:
    numbers = [line.rstrip() for line in f]

i = 0
c_index_1 = 0
c_index_2 = 0
first_component = 0
second_component = 0
third_component = 0
while True:
    j = i + 1
    
    while j < len(numbers):
        
        k = j + 1
        first_component = int(numbers[i])
        second_component = int(numbers[j])
        
        while k < len(numbers):
            third_component = int(numbers[k])
            if(  first_component + second_component + third_component == 2020 ):
                break
            
            k += 1

        if( k < len(numbers) ):
            break


        j += 1
        
 
    if( j < len(numbers) ):
        break

    i += 1

print(first_component*second_component*third_component)