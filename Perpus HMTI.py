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
