with open('day_04_input.txt') as f:
    passports = [line.rstrip() for line in f]

i = 0
no_of_valid_passports = 0
while i < len(passports):

    passport_valid = True
    
    passport = ""

    while i < len(passports) and passports[i] != '':
        passport += passports[i]
        i += 1

#    print(passport)

    if( passport.find('byr:') == -1):
        passport_valid = False
    elif( passport.find('iyr:') == -1):
        passport_valid = False
    elif( passport.find('eyr:') == -1 ):
        passport_valid = False
    elif( passport.find('hgt:') == -1 ):
        passport_valid = False
    elif( passport.find('hcl:') == -1 ):
        passport_valid = False
    elif( passport.find('ecl:') == -1 ):
        passport_valid = False
    elif( passport.find('pid:') == -1 ):
        passport_valid = False

    if( passport_valid ):
        no_of_valid_passports += 1
    
    i += 1

print(no_of_valid_passports)
