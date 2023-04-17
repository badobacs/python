def get_unique_answer(response):
    questions = []
    for char in response:
        if char not in questions:
            questions.append(char)
    return len(questions)


with open('input6.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]


sum = 0
currentRes = ''
for line in data:
    if line != '':
        currentRes +=line
    else:
        sum += get_unique_answer(currentRes)
        currentRes = ''
sum += get_unique_answer(currentRes)
print(sum)
# part2
def get_total_answer(responses):
    questions = []
    
    for char in responses[0]:
        allLines = True
        for line in responses:
            if char not in line:
               allLines = False
        if allLines and char not in questions:
           questions.append(char)
           
sum = 0
currentRes = []
for line in data:
    if line != '':
        currentRes.append(line)
    else:
        sum += get_unique_answer(currentRes)
        currentRes = []
sum += get_unique_answer(currentRes)
print(sum)