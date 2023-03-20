n=int(input())
legnagyobb=0
legnagyobb_ind=0
for i in range(n):
    a=input()
    a=a.split(' ')
    ar=int(a[1])
    t=int(a)
    if legnagyobb<ar:
        legnagyobb=ar
        legnagyobb_ind=i+1
print(legnagyobb_ind)
