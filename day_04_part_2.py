with open('day_04_input.txt') as f:
#    passports = [line.rstrip() for line in f]
    passports = f.readlines()

i = 0
no_of_valid_passports = 0
while i < len(passports):

    passport_valid = True
    
    passport = ""

    while i < len(passports) and passports[i] != '\n':
        passport += passports[i]
        i += 1

#    print(passport)

    byr_index = passport.find('byr:')
    iyr_index = passport.find('iyr:')
    eyr_index = passport.find('eyr:')
    hgt_index = passport.find('hgt:')
    hcl_index = passport.find('hcl:')
    ecl_index = passport.find('ecl:')
    pid_index = passport.find('pid:')

    
    if( byr_index != -1 ):
        
        byr = ''
        byr_index += 4 
        
        while byr_index < len(passport) and ( passport[byr_index] != ' ' and passport[byr_index] != '\n'):
            byr += passport[byr_index]
            byr_index += 1
        
        if( len(byr) != 4 or (int(byr) < 1920 or 2002 < int(byr))):
            passport_valid = False
#            print("byr is: " + str(byr))
    else:
        passport_valid = False
 #       print("no byr")


    if( iyr_index != -1 and passport_valid ):        
        iyr = ''
        iyr_index += 4 
        
        while iyr_index < len(passport) and ( passport[iyr_index] != ' ' and passport[iyr_index] != '\n'):
            iyr += passport[iyr_index]
            iyr_index += 1
        
        if( len(iyr) != 4 or (int(iyr) < 2010 or 2020 < int(iyr))):
            passport_valid = False
#            print("iyr is: " + str(iyr))
    else:
        passport_valid = False
#        print("no iyr")

    if( eyr_index != -1 and passport_valid ):
        eyr = ''
        eyr_index += 4 
        
        while eyr_index < len(passport) and ( passport[eyr_index] != ' ' and passport[eyr_index] != '\n'):
            eyr += passport[eyr_index]
            eyr_index += 1

      
        if( len(eyr) != 4 or (int(eyr) < 2020 or 2030 < int(eyr))):
            passport_valid = False
#            print("eyr invalid! eyr is: " + str(eyr))
    else:
        passport_valid = False
#        print("no eyr")

    if( hgt_index != -1 and passport_valid ):
        hgt = ''
        hgt_index += 4 

        while hgt_index < len(passport) and ( passport[hgt_index] != ' ' and passport[hgt_index] != '\n'):
            hgt += passport[hgt_index]
            hgt_index += 1
        
#        print("height check starting with: " + hgt)        

        if( hgt[-2:] == 'in' or hgt[-2:] == 'cm' ):
            j=0
            height = ''
            while hgt[j] != 'c' and  hgt[j] != 'i':
                height += hgt[j]
                j += 1
            
#            print("height is: " + height)

            if( (hgt[-2:] == 'in' and (int(height) < 59 or int(height) > 76 ))):
                passport_valid = False
            elif(hgt[-2:] == 'cm' and (int(height) < 150 or int(height) > 193) ):
                passport_valid = False
        else:
            passport_valid = False

 #       print("this height wast: " + str(passport_valid))
    else:
        passport_valid = False

    if( hcl_index != -1 and passport_valid ):
        hcl = ''
        hcl_index += 4 
        
        while hcl_index < len(passport) and ( passport[hcl_index] != ' ' and passport[hcl_index] != '\n'):
            hcl += passport[hcl_index]
            hcl_index += 1

        if( len(hcl) != 7 or hcl[0] != '#'):
            passport_valid = False
  #          print("hair colour not valid! Hair colour is: " + str(hcl))
        
        if( passport_valid ):
            index_of_char = 1

            checklist = [None] * 10 

            number = 0
            while number < 10:
                checklist[number] = str(number)
                number +=1

            while index_of_char < len(hcl) and passport_valid:
                if( (hcl[index_of_char] not in ['a', 'b', 'c', 'd', 'e','f']) and hcl[index_of_char] not in checklist):
                    passport_valid = False
#                    print("hair colour not valid! Hair colour is: " + str(hcl))
                    break
                index_of_char += 1
    else:
        passport_valid = False
 #       print("No hair colour")

    if( ecl_index != -1 and passport_valid ):
        ecl = ''
        ecl_index += 4 
        
        while ecl_index < len(passport) and ( passport[ecl_index] != ' ' and passport[ecl_index] != '\n'):
            ecl += passport[ecl_index]
            ecl_index += 1

        checklist = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if( ecl not in checklist):
            passport_valid = False
 #           print("Eye colour not valid! Eye colour is: " + str(ecl))
    else:
        passport_valid = False
        
    if( pid_index != -1 and passport_valid ):
        pid = ''
        pid_index += 4 
        
        while pid_index < len(passport) and ( passport[pid_index] != ' ' and passport[pid_index] != '\n'):
            pid += passport[pid_index]
            pid_index += 1

        if( len(pid) != 9):
            passport_valid = False
    
        checklist = [None] * 10 
        number = 0
        while number < 10:
            checklist[number] = str(number)
            number +=1

        index_of_char = 0
        while index_of_char < len(hcl) and passport_valid:
            if( pid[index_of_char] not in checklist):
                passport_valid = False
                break
            index_of_char += 1

    else:
        passport_valid = False

    if( passport_valid ):
        no_of_valid_passports += 1
    
    i += 1

print(no_of_valid_passports)
