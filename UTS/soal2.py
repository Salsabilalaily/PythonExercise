def Push(Stack,jumlah,warna):
  banyak = int(jumlah)
  for i in range (banyak):
    Stack.append(warna)

def Pop(Stack,jumlah):
  banyak = int(jumlah)  
  for i in range(banyak):
      del (Stack[-1])
   
def PrintStack (Stack):
  n =len(Stack)
  hitam = 0
  putih = 0
  print()
  for i in range (n-1,-1,-1):
    if (Stack[i] == "H"):
        hitam = hitam + 1
    else :
        putih = putih + 1
  print(hitam , " " , putih  )



x = int(input())

tumpukan = []

for i in range(x):
    masukan = list(input().split())
    
    if (masukan[0] == "0"):
        Push(tumpukan, masukan[1] , masukan[2] )

    elif (masukan[0] == "1"):
        Pop(tumpukan, masukan[1]) 
        
PrintStack(tumpukan)
