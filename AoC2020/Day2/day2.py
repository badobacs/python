import csv

with open('input2.csv') as data:
    reader = csv.reader(data, delimiter=' ')
    for row in reader:
        policy, letter, password = row[0], row[1][0], row[2]
        i = policy.index('-')
        low = policy[:1]
        high = policy[i+1:]
        print(policy, low, high)
        
