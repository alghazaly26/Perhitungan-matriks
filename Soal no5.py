#Fungsi pada elemen (n, values, dp)
def island_vacation():
    n = int(input())
    values = list(map(int, input().split()))
    
    dp = [0] * n
    dp[0] = values[0]
    dp[1] = max(values[0], values[1])
    
    #Mencari rata-rata pada (2, n):
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + values[i])
    
    #Lakukan pencetakan
    print(dp[-1])

island_vacation()

'''
Mulai
Algoritma kompleksitas waktu
Membaca input n membutuhkan waktu O(1).
Membaca dan memetakan values membutuhkan waktu O(n) karena ada n elemen.
Menginisialisasi array dp dengan n elemen membutuhkan waktu O(n).
Menginisialisasi elemen pertama dp[0] dan elemen kedua dp[1] masing-masing membutuhkan waktu O(1).
Loop ini berjalan dari i = 2 hingga i = n-1, sehingga iterasinya adalah O(n-2) yang setara dengan O(n).
Dalam setiap iterasi, operasi max(dp[i-1], dp[i-2] + values[i]) membutuhkan waktu O(1).
Total kompleksitas waktu dari algoritma ini adalah kombinasi dari semua bagian yang relevan:

Membaca input dan memetakan nilai: O(n)
Inisialisasi array dp: O(n)
Loop untuk mengisi tabel DP: O(n)
Mencetak hasil: O(1)
Total kompleksitas waktu dari fungsi island_vacation() adalah O(n).
Selesai
'''