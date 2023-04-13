fields=['byr', 'iyr','eyr','hgt','hcl','ecl','pid']
validPass = []

def valid_passport(pp):
    for field in fields:
        if field not in pp:
            return False
        return True

with open('input4.txt') as file:
   data = file.readlines() 
   data=[line.strip() for line in data]
#    print (data)
validCount = 0

currentPassport = ''
for line in data:
    if line != '':
        currentPassport += ' ' + line
    else:
        if valid_passport(currentPassport):
            validPass.append(currentPassport)
            validCount += 1
        currentPassport = ''
if valid_passport(currentPassport):
    validPass.append(currentPassport)
    validCount += 1
print(validCount)

# part2

def is_valid_byr(byr):
    byr = int(byr)
    if byr <1920 or byr >2002:
        return False
    return True

def is_valid_iyr(iyr):
    iyr = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False
    return True

def is_valid_eyr(eyr):
    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False
    return True

def is_valid_hgt(hgt):
    units = hgt[-2:]
    if units not in ['in','cm']:
        return False
    hgt = int(hgt[:-2])
    if units == 'in':
        if hgt <69 or hgt > 76:
            return False
    elif units == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    return True
            
def is_valid_hcl(hcl):
    if hcl[0] != '#':
        return False
    if len(hcl[1:]) != 6: return False
        

def is_valid_ecl(ecl):
    colors = ['amb','blu','brn','gry','grn','hzl','oth']
    # if ecl != 'amb' or 'blu' or 'brn' or 'gry' or 'grn' or 'hzl' or 'oth':
    if ecl not in colors:
        return False
    return True

def is_valid_pid(pid):
    if len(pid) != 9:
        return False
    return True

def real_val_data(passP):
    passP = passP.split()
    data = {}
    for item in passP:
        key = item[:3]
        value = item[4:]
        data[key] = value
    
    if not is_valid_byr(data['byr']):
        return False
    if not is_valid_iyr(data['iyr']):
        return False
    if not is_valid_eyr(data['eyr']):
        return False
    if not is_valid_hgt(data['hgt']):
        return False
    if not is_valid_hcl(data['hcl']):
        return False
    if not is_valid_ecl(data['ecl']):
        return False
    if not is_valid_pid(data['pid']):
        return False
    return True
validCount = 0
for pp in valid_passport:
    if real_val_data(pp):
        validCount +=1
print(validCount)