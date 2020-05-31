class Perpustakaan:
    def __init__(self, list, nama):
        self.ListBuku = list
        self.nama = nama
        self.BukuTerpinjam = {}

    def displayBuku(self):
        print(f"Berikut merupakan daftar buku yang dimiliki Perpustakaan {self.nama}")
        for buku in self.ListBuku:
            print(buku)

    def PinjamBuku(self, user, buku):
        if buku not in self.BukuTerpinjam.keys():
            self.BukuTerpinjam.update({buku:user})
            print("Perpustakaan HMTI telah berhasil merekam peminjaman")
        else:
            print(f"Maaf, buku ini telah dipinjam oleh {self.BukuTerpinjam[buku]}")

    def TambahBuku(self, buku):
        self.ListBuku.append(buku)
        print("buku telah ditambahkan ke dalam list")

    def KembalikanBuku(self, buku):
        self.BukuTerpinjam.pop(buku)
       
if __name__ == '__main__':
    hmti = Perpustakaan(['Al-Quran', 'Al-kitab', 'Weda', 'Tripitaka', 'Shishu Wujing'], "HMTI")

    while (True):
        print("======================================================================================")
        print(f"|  Selamat datang di Perpustakaan {hmti.nama}. Silahkan pilih menu untuk melanjutkan        |")
        print("|  1. Tampilkan buku                                                                 |")
        print("|  2. Pinjamkan buku                                                                 |")
        print("|  3. Tambahkan buku                                                                 |")
        print("|  4. Kembalikan buku                                                                |")
        print("======================================================================================")
        user_choice = input("Input = ")
        if user_choice not in ['1', '2', '3', '4']:
            print("!!!Tolong masukkan nomor opsi menu yang tersedia!!!")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            hmti.displayBuku()

        elif user_choice == 2:
            buku = input("Masukkan judul buku yang ingin dipinjamkan \nInput = ")
            user = input("Masukkan nama peminjam \nInput = ")
            hmti.PinjamBuku(user, buku)

        elif user_choice == 3:
            buku = input("Masukkan judul buku yang ingin ditambahkan \nInput = ")
            hmti.TambahBuku(buku)

        elif user_choice == 4:
            buku = input("Masukkan judul buku yang ingin dikembalikan \nInput = ")
            hmti.KembalikanBuku(buku)

        else:
            print("Opsi yang dimasukkan tidak valid")

        print("\nTekan K untuk keluar dan L untuk lanjut")
        user_choice2 = ""
        while(user_choice2!="L" and user_choice2!="K"):
            user_choice2 = input()
            if user_choice2 == "K":
                exit()

            elif user_choice2 == "L":
                continue

