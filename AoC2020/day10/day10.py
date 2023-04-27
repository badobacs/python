with open('input10.txt') as file:
    data = [ int(line.strip()) for line in (file.readlines()) ]
    data.sort()
data = [0] + data
data.append(max(data)+3)

def get_diff_count():
    count1 = 0
    count2 = 0
    
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        
        if diff == 1:
            count1 += 1
        elif diff == 3:
            count2 += 1
    return count1 * count2 

print(get_diff_count())
    