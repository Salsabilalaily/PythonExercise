gen1=input()
gen2=input()
x=(input())
hasil=""

for i in range (len(x)):
    if x[i]=='0':
        hasil+=gen1[i]
    else:
        hasil+=gen2[i]
print(hasil)
