with open('input1.txt') as file:
    lists=file.readlines()

numbs = [int(list.strip()) for list in lists]

largest =-1
for i in range(len(numbs)-1):
    for j in range(i+1,len(numbs)):
        numb1=numbs[i]
        numb2=numbs[j]
        if numb1+numb2==2020:
            balance=numb1*numb2
            if balance >largest:
                largest=balance
print(largest)

largest =-1
for i in range(len(numbs)-1):
    for j in range(i+1,len(numbs)):
        for k in range(j+1,len(numbs)):
            numb1, numb2, numb3 = numbs[i], numbs[j], numbs[k]
            if numb1+numb2+numb3 ==2020:
                balance=numb1*numb2*numb3
            if balance >largest:
                largest=balance
print(largest)
