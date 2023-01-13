MatriksA = [[1,0], [0,1]]
print(MatriksA)

matriksA = [[1, 2, 0],[2, 2, 1],[0, 3, 3]]

print('Matriks A')
for x in range(0, len(matriksA)):
    for y in range(0, len(matriksA[0])):
        print(matriksA[x][y], end=' '),
    print()

matriksB = [[-1, 5],[3, 1],[0, 1]]

print('Matriks B')
for x in range(0, len(matriksB)):
    for y in range(0, len(matriksB[0])):
        print(matriksB[x][y], end=' '),
    print()

hasilKali = []

for x in range(0, len(matriksA)):
    baris = []
    for y in range(0, len(matriksB[0])):
        count = 0
        for z in range(0, len(matriksB)):
            count = count + (matriksA[x][z] * matriksB[z][y])
        baris.append(count)
        hasilKali.append(baris)

print('Hasil Kali Matriks A dan B')
for x in range(0, len(hasilKali)):
    for y in range(0, len(hasilKali[0])):
        print (hasilKali[x][y], end=' ')
    print ()