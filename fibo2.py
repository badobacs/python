n = int(input("What's the number?"))

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nt=10

if nt <=0:
    nt *= -1
else:
   print("Fibonacci sequence:")
   for i in range(nt):
       print(recur_fibo(i))