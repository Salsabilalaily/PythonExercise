n=int(input())
for i in range(0,n):
    masukkan=str(input())

    for j in range(len(masukkan)):
        if j%2==0:
            print(masukkan[j], end="")
    print(" ", end="")
    
    for j in range(len(masukkan)):
        if j%2!=0:
            print(masukkan[j],end="")
    print("")
