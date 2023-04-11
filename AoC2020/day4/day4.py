fields=['byr', 'iyr','eyr','hgt','hcl','ecl','pid']

def valid_passport(pp):
    for field in fields:
        if field not in pp:
            return False
        return True

with open('input4.txt') as file:
   data = file.readlines() 
print (data)