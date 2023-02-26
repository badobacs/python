# def ossze(a,b):
#     return a+b


# print(ossze(1,4))

a =int(input())
b =int(input())

def osszegzes(a,b):
    osszeg=0
    for i in range(a+1,b):
        osszeg+=i   
    print(osszeg)
osszegzes(a,b)   

koztu_szamok_ossz=osszegzes(1,9)
print(koztu_szamok_ossz)   

def oszegzes3(a,b):
    sum(range(a+1,b)) 
lista=[1,5,3]
print(sum(lista))
    