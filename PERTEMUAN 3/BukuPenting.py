#BUKU PENTING
def isEmpty():
    return kode==[]

n=int(input())
kode=[]
judul=[]

for i in range(n):
    masukkan=list(input().split())
    
    if masukkan[0]=='T':
        kode.append(masukkan[1])
        judul.append(masukkan[2])
    elif not isEmpty() and masukkan[0]=='A':
        kode.pop()
        judul.pop()
        
for i in range(len(kode)):
    print(kode.pop(), judul.pop())
