import csv

with open('input2.csv') as data:
    reader = csv.reader(data, delimiter=' ')
    validCount = 0
    for row in reader:
        policy, letter, password = row[0], row[1][0], row[2]
        
        i = policy.index('-')
        low = int(policy[:i])
        high = int(policy[i+1:])
        
        count = 0
        for character in password:
            if character == letter:
                count += 1
        if count>= low and count<= high:
            validCount += 1
    print(validCount)
    
    # part2
with open('input2.csv') as data:
    reader = csv.reader(data, delimiter=' ')
    validCount = 0
    for row in reader:
        policy, letter, password = row[0], row[1][0], row[2]
        
        i = policy.index('-')
        low = int(policy[:i])
        high = int(policy[i+1:])
        
        count = 0
        first = password[low-1] == letter
        last = password[high-1] == letter
        if (first and not last) or(last and not first):
            validCount += 1
    print(validCount)
