#Fungsi pada elemen (n,p)
def gaus_electronics():
    n = int(input())
    p = list(map(int, input().split()))
    
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    #Mencari nilai rata-rata pada (2, n + 1):
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    
    #Lakukan pencetakan 
    print(m[1][n])

gaus_electronics()

'''
Mulai
algoritma kompleksitas waktu
Input:

n adalah jumlah matriks yang akan dikalikan.
p adalah daftar ukuran matriks di mana p[i-1] x p[i] adalah ukuran dari matriks ke-i.
Dynamic Programming Table:

m adalah tabel DP (Dynamic Programming) yang digunakan untuk menyimpan biaya minimum dari perkalian matriks. m[i][j] menyimpan biaya minimum untuk mengalikan matriks dari i ke j.
Algoritma:

Mengisi tabel DP m berdasarkan panjang rantai matriks (L).
Iterasi melalui semua kemungkinan sub-problem untuk menemukan solusi optimal.
Biaya q dihitung sebagai jumlah dari dua sub-problem dan biaya untuk menggabungkan hasil dari dua sub-problem tersebut.
Simpan nilai minimum dalam tabel m.

Inisialisasi:
Tabel m diinisialisasi dengan 0 karena biaya untuk mengalikan satu matriks dengan dirinya sendiri adalah 0.

Pengisian Tabel:
Pengisian tabel dilakukan secara bertahap dari panjang rantai matriks yang kecil ke panjang yang lebih besar, sehingga setiap sub-problem diselesaikan sebelum digunakan dalam penyelesaian masalah yang lebih besar.

Kompleksitas Waktu:
Algoritma ini berjalan dalam waktu O(n^3) karena ada tiga loop bersarang.
Selesai
'''