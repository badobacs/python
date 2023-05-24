with open('input11.txt') as file:
    data =file.readlines()
    data = [ list(line.strip()) for line in (data) ]
    
print(data)