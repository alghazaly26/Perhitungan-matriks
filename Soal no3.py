#Fungsi pada node
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

#Fungsi pada head
def print_list(head):
    current = head
    while current:
        print(current.name, end='')
        if current.next:
            print(' -> ', end='')
        current = current.next
    #Melakukan pencetakan pada elemen berupa current.name, end
    print()

johnny = Node('Johnny')
mark = Node('Mark')
joshua = Node('Joshua')
lisa = Node('Lisa')
jennie = Node('Jennie')

johnny.next = mark
mark.next = joshua
joshua.next = lisa
lisa.next = jennie

print_list(johnny)

'''
Mulai
nisialisasi sebuah objek Node membutuhkan waktu O(1) karena hanya mengatur dua atribut (name dan next).
Fungsi ini berjalan melalui linked list dari node head hingga node terakhir.
Loop while current akan berjalan n kali, di mana n adalah jumlah node dalam linked list.
Dalam setiap iterasi, operasi print(current.name, end=''), if current.next, dan current = current.next masing-masing membutuhkan waktu O(1).
Jadi, waktu total untuk fungsi print_list adalah O(n), di mana n adalah jumlah node dalam linked list.
Membuat 5 objek Node masing-masing membutuhkan waktu O(1), sehingga total waktu adalah O(5) = O(1).
Menghubungkan node-node tersebut (johnny.next = mark, dll.) masing-masing membutuhkan waktu O(1), sehingga total waktu adalah O(4) = O(1)
Membuat node dan menghubungkannya: O(1)
Fungsi print_list yang mencetak linked list: O(n)
Total kompleksitas waktu dari seluruh program adalah O(n).
Selesai
'''