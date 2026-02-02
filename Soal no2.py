#Fungsi karakter pada min_operations(A, B):
def min_operations(A, B):
    N = len(A)
    operations = 2
    i = 0
    while i < N:
        if A[i] > B[i]:
            j = i + 1
            while j < N and A[j] <= B[j]:
                j += 1
            operations += 1
            i = j - 1
        i += 1
    #Pemanggilan pada karakter operations
    return operations

N = int(input())
A = input('bandung')
B = input('jakarta')
#lakukan pencetakan
print(min_operations(A, B))

'''
Mulai
Kita membaca string masukan A dan B dan menyimpannya dalam variabel.
Kami mendefinisikan fungsi min_operations untuk menghitung jumlah minimum operasi yang diperlukan.
Kami mengulangi string A dan B dari kiri ke kanan.
Kompleksitas waktu dari solusi ini adalah O(N), dimana N adalah panjang string A dan B.
Pendekatan serakah berhasil karena kami selalu berusaha menukar jumlah minimum karakter yang diperlukan untuk membuat Ai ≤ Bi. Dengan melakukan ini, kami meminimalkan jumlah operasi yang diperlukan.
Selesai
'''