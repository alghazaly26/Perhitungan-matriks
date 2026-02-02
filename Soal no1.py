import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        dist, node = heapq.heappop(pq)
        for neighbor, weight in graph[node].items():
            old_dist = distances[neighbor]
            new_dist = dist + weight
            if new_dist < old_dist:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

def calculate_average_visits(graph, A, B):
    distances_A = dijkstra(graph, A)
    distances_B = dijkstra(graph, B)
    average_visits = [0] * len(graph)
    for node in range(1, len(graph) + 1):
        shortest_path_A = distances_A[node]
        shortest_path_B = distances_B[node]
        if shortest_path_A!= float('inf') and shortest_path_B!= float('inf'):
            average_visits[node - 1] = 2 / (shortest_path_A + shortest_path_B)
    return average_visits

N, M, A, B = map(int, input().split())
graph = {node: {} for node in range(1, N + 1)}
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

average_visits = calculate_average_visits(graph, A, B)
for visit in average_visits:
    print(int(visit))

'''
Mulai
Kita membaca grafik input dan menyimpannya dalam grafik kamus di mana setiap kunci adalah sebuah node dan nilainya adalah kamus tetangganya dan bobotnya.
tentukan fungsi hitung_rata-rata_visit untuk menghitung jumlah rata-rata kunjungan ke setiap gedung. Kami menggunakan fungsi dijkstra untuk menghitung jarak terpendek dari rumah Molly (A) dan rumah Bella (B) ke semua node lainnya. Kemudian, kita menghitung jumlah rata-rata kunjungan ke setiap node dengan mengambil kebalikan dari jumlah jarak terpendek dari A dan B, dan mengalikannya dengan 2 karena Molly mengunjungi setiap node dua kali (sekali dalam perjalanan ke rumah Bella dan sekali di jalan). jalan kembali).
Kompleksitas waktu dari solusi ini adalah O(N log N + M) karena algoritma Dijkstra, dan kompleksitas ruang adalah O(N + M) untuk menyimpan grafik dan jarak.
Selesai
'''