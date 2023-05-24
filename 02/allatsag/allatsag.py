# N = int(input())
# eladas=0
# T=[]
# for i in range(N):
#     T.append(int(input()))

# # for j in range(T):
# #    if T[j] > T[j-1]:
# #        eladas += 1
# print(T)


sale_number = int()
S=[]
with open('be1.txt') as file:
    sales=file.read()
    for i in sales:
        
        print(str(sales[i]))