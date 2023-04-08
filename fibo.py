x = int(input("How long do you want to?"))
n1= int(input("what i the beginner number?"))
n2 = n1+ (n1/2)
count = 0

# ellenörizzük a szám érvényességét
if x < 0:
    x *= -1

# ha 1 jegyüt kér visszaadjuk az elsö elemet
elif x  == 1:
    print("Fibonacci sequence upto",x,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < x:
        print(n1)
        nx=n1+n2
        n1=n2
        n2=nx
        count +=1
