#Fungsi (n):
def tailor_swift(n):
    orders = []
    #Mencari rata-rata (n):
    for _ in range(n):
        name, profit, time, deadline = input().split()
        profit = int(profit)
        time = int(time)
        deadline = int(deadline)
        orders.append((deadline, profit, time, name))
    orders.sort()
    total_profit = 0
    schedule = []
    for deadline, profit, time, name in orders:
        if time <= deadline:
            total_profit += profit
            schedule.append(name)
    print(' '.join(schedule))
    print(total_profit)

n = int(input())
tailor_swift(n)

'''
Mulai
Baca pesanan yang dimasukkan dan simpan dalam daftar tupel, yang mana setiap tupel berisi batas waktu, keuntungan, waktu, dan nama pesanan.
Urutkan pesanan berdasarkan tenggat waktunya dalam urutan menaik. (Kompleksitas waktu: O(n log n))
Initialize a variable total_profit to 0 and an empty list schedule to store the selected orders.
Kompleksitas waktu: O(n log n) karena penyortiran pesanan.
Kompleksitas ruang: O(n) untuk menyimpan pesanan dan jadwal.
Selesai
'''