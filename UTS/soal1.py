def output(n):
    a = int(n)
    if n>(a+0.5) :
        print(a+1)
    else:
        print(a)

n = int(input())
count = 0

count = n/1500
if count>=5 :
    n=n-1500*5
    count = n/600
    if count>=7 :
        n=n-600*7
        count = n/200 + 12
    else:
        count = count + 5
    
output(count)
