import csv
import os

csv_filename = 'databuku.csv'

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')


class Perpustakaan:
    
    def __init__(self, nama):
        
        self.nama = nama

    def displayBuku(self):
        
        print(f"Berikut merupakan daftar buku yang dimiliki Perpustakaan {self.nama}")
        self.databuku = []
    
        with open(csv_filename, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.databuku.append(row)
            
        print("NO \t JUDUL BUKU \t\t\t PENGARANG \t\t PEMINJAM")
        print("-" * 74)

        for data in self.databuku:
            print(f"{data['NO']} \t {data['JUDUL BUKU']} \t\t {data['PENGARANG']}\t\t {data['PEMINJAM']}")

        print("-" * 74)
                  

    def PinjamBuku(self):
                  
        self.databuku = []
        hmti.displayBuku()
        no = input("Masukkan nomor urut buku yang ingin dipinjamkan:  ")
        peminjam = input("Masukkan nama peminjam:  ")

        indeks = 0
        for data in self.databuku:
            if (data['NO'] == no):
                self.databuku[indeks]['PEMINJAM'] = peminjam
            indeks = indeks + 1

        with open(csv_filename, mode="w") as csv_file:
            fieldnames = ['NO', 'JUDUL BUKU', 'PENGARANG', 'PEMINJAM']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in self.databuku:
                writer.writerow({'NO': new_data['NO'], 'JUDUL BUKU': new_data['JUDUL BUKU'], 'PENGARANG': new_data['PENGARANG'], 'PEMINJAM': new_data['PEMINJAM']}) 

        loop=True
        count=1
        while loop==True:
            choice=str(input("Apakah ada buku lain yang ingin dipinjam? Tekan Y untuk yes dan tekan N untuk no:  "))
            if(choice.upper()=="Y"):
                count=count+1
                no = input("Masukkan nomor urut buku yang ingin dipinjamkan:  ")
                indeks = 0
                for data in self.databuku:
                    if (data['NO'] == no):
                        self.databuku[indeks]['PEMINJAM'] = peminjam
                    indeks = indeks + 1

                with open(csv_filename, mode="w") as csv_file:
                    fieldnames = ['NO', 'JUDUL BUKU', 'PENGARANG', 'PEMINJAM']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in self.databuku:
                        writer.writerow({'NO': new_data['NO'], 'JUDUL BUKU': new_data['JUDUL BUKU'], 'PENGARANG': new_data['PENGARANG'], 'PEMINJAM': new_data['PEMINJAM']})
                loop=False
                break
            elif (choice.upper()=="N"):
                print("")
                loop=False
            else:
                print("Pilihan yang dimasukkan salah")

        print("Buku sudah terpinjam")


    def TambahBuku(self, no, judul_buku, pengarang):
                  
        with open(csv_filename, mode='a') as csv_file:
            fieldnames = ['NO', 'JUDUL BUKU', 'PENGARANG']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'NO': no, 'JUDUL BUKU': judul_buku, 'PENGARANG': pengarang})
            print("Buku telah ditambahkan ke dalam list")
                  

    def KembalikanBuku(self):
                  
        self.databuku = []
        hmti.displayBuku()
        no = input("Nomor buku yang ingin dikembalikan: ")
        peminjam = 0

        indeks = 0
        for data in self.databuku:
            if (data['NO'] == no):
                self.databuku[indeks]['PEMINJAM'] = peminjam
            indeks = indeks + 1

        with open(csv_filename, mode="w") as csv_file:
            fieldnames = ['NO', 'JUDUL BUKU', 'PENGARANG', 'PEMINJAM']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in self.databuku:
                writer.writerow({'NO': new_data['NO'], 'JUDUL BUKU': new_data['JUDUL BUKU'], 'PENGARANG': new_data['PENGARANG'], 'PEMINJAM': new_data['PEMINJAM']})

        print("Buku sudah dikembalikan")
        
       
if __name__ == '__main__':
    hmti = Perpustakaan("HMTI")
    
    while (True):
        clear_screen()
        print("======================================================================================")
        print(f"|  Selamat datang di Perpustakaan {hmti.nama}. Silahkan pilih menu untuk melanjutkan        |")
        print("|  1. Tampilkan buku                                                                 |")
        print("|  2. Pinjamkan buku                                                                 |")
        print("|  3. Tambahkan buku                                                                 |")
        print("|  4. Kembalikan buku                                                                |")
        print("======================================================================================")
        user_choice = input("Input = ")
        if user_choice not in ['1', '2', '3', '4', '0']:
            print("!!!Tolong masukkan nomor opsi menu yang tersedia!!!")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            hmti.displayBuku()

        elif user_choice == 2:
            hmti.PinjamBuku()

        elif user_choice == 3:
            hmti.displayBuku()
            no = input("NO: ")
            judul_buku = input("JUDUL BUKU: ")
            pengarang = input("PENGARANG: ")
            hmti.TambahBuku(no, judul_buku, pengarang)

        elif user_choice == 4:
            hmti.KembalikanBuku()
        
        elif user_choice == 0:
            exit()

        else:
            print("Opsi yang dimasukkan tidak valid")

        print("\n")
        input("Tekan tombol apa saja untuk kembali...")
        continue

