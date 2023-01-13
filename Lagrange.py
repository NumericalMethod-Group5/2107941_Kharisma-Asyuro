# Menampilkan library numpy yang fokus pada scientific computing
import numpy as np

# Membaca jumlah data yang akan diinput oleh user
n = int(input('Masukkan jumlah data / titik poin: '))

# Membuat array dari numpy berdasarkan data yang diinputkan dan melakukan inisialisasi ke 0 untuk menyimpan nilai x dan y dengan menggunakan tabel selisih terbagi
nilaiX = np.zeros((n))
nilaiY = np.zeros((n))

print('Masukan data X dan Y: ')
for i in range(n):
    nilaiX[i] = float(input( 'nilaiX['+str(i)+']='))
    nilaiY[i] = float(input( 'nilaiY['+str(i)+']='))

# Membaca titik yang diinterpolasi
nilaiXP = float(input('Masukkan titik interpolasi: '))

# Mengatur nilai fungsi dari titik interpolasi ke 0
nilaiYP = 0

# Implementasi dari Metode Lagrange
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (nilaiXP - nilaiX[j])/(nilaiX[i] - nilaiX[j])
    nilaiYP = nilaiYP + p * nilaiY[i]    

# Menampilkan hasil
print('Nilai interpolasi untuk titik %.3f adalah %.3f.' % (nilaiXP, nilaiYP))