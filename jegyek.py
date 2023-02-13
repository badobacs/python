N=int(input())

jegyek=[]
for i in range(N):
    #a lista végére hozzáteszi a beolvasott számot
    jegyek.append(int(input()))
jegyek_db =[0,0,0,0,0]
# print(jegyek) 
for jegy in jegyek:
    jegyek_db[jegy-1]+=1
    # if jegy==1:
    #     j1+=j1
    # elif jegy == 2:
    #     j2+=j2

# print(jegyek_db)
for j_db in jegyek_db:
    print(j_db, end="")
    