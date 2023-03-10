import numpy as np
import sys

number = int(input('Masukan angka untuk ukuran matriks: '))
matriksA = np.zeros((number,number+1))
matriksHasil = np.zeros(number)
print('Masukan Nilai Koefisien Penjumlahan Matriks:')
for i in range(number):
    for j in range(number+1):
        matriksA[i][j] = float(input( 'matriksA['+str(i)+']['+ str(j)+']='))

for i in range(number):
    if matriksA[i][i] == 0.0:
        sys.exit('Mendeteksi Pembagian dengan 0!')
        
    for j in range(number):
        if i != j:
            ratio = matriksA[j][i]/matriksA[i][i]

            for k in range(number+1):
                matriksA[j][k] = matriksA[j][k] - ratio * matriksA[i][k]


for i in range(number):
    matriksHasil[i] = matriksA[i][number]/matriksA[i][i]
print('\nSolusi yang ditemukan adalah : ')
for i in range(number):
    print('X%d = %0.2f' %(i,matriksHasil[i]), end = '\t')