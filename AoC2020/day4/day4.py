fields=['byr', 'iyr','eyr','hgt','hcl','ecl','pid']

def valid_passport(pp):
    for field in fields:
        if field not in pp:
            return False
        return True

with open('input4.txt') as file:
   data = file.readlines() 
   data=[line.strip() for line in data]
   print (data)
validCount = 0

currentpasport = ''
for line in data:
    if line != '':
        currentpasport += ' ' + line
    else:
        if valid_passport(currentpasport):
            validCount += 1
        currentpasport = ''
if valid_passport(currentpasport):
    validCount += 1
print(validCount)