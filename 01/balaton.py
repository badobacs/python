N = int(input())
ice = []
for i in range(N):
    ice.append(int(input()))

iced = 0

for x in range(len(ice)):
    if ice[x] > 0:
        iced += 1

print(iced)