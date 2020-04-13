volume = int(input())

botolBesar = [0]*5
botolSedang = [0]*7
botolKecil = [0]*9

kapasitasBesar = 1500
kapasitasSedang = 600
kapasitasKecil = 200

for i in range (len(botolBesar)):
    if (volume > 0):
        if (volume > kapasitasBesar):
            botolBesar[i] = kapasitasBesar
        else:
            botolBesar[i] = volume
        volume = volume - botolBesar[i]

for i in range (len(botolSedang)):
    if (volume > 0):
        if (volume > kapasitasSedang):
            botolSedang[i] = kapasitasSedang
        else:
            botolSedang[i] = volume
        volume = volume - botolSedang[i]
        
for i in range (len(botolKecil)):
    if (volume > 0):
        if (volume > kapasitasKecil):
            botolKecil[i] = kapasitasKecil
        else:
            botolKecil[i] = volume
        volume = volume - botolKecil[i]

lebihDariSetengah = 0
for volume in botolBesar:
    if volume > kapasitasBesar/2:
        lebihDariSetengah += 1
for volume in botolSedang:
    if volume > kapasitasSedang/2:
        lebihDariSetengah += 1
for volume in botolKecil:
    if volume > kapasitasKecil/2:
        lebihDariSetengah += 1

print(lebihDariSetengah)
