from datetime import datetime, timedelta

class Buku:
    def __init__(self, id_buku, judul, penulis, tersedia=True):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tersedia = tersedia
    
    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False
    
    def kembalikan(self):
        self.tersedia = True
    
    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} oleh {self.penulis} - {status}"


class Anggota:
    MAKS_HARI_PINJAM = 7  # Maksimal 7 hari peminjaman
    DENDA_PER_HARI = 2000  # Denda keterlambatan per hari

    def __init__(self, id_anggota, nama):
        self.id_anggota = id_anggota
        self.nama = nama
        self.buku_dipinjam = {}
    
    def pinjam_buku(self, buku):
        if buku.pinjam():
            tanggal_pinjam = datetime.now()
            self.buku_dipinjam[buku] = tanggal_pinjam
            print(f"{self.nama} telah meminjam {buku.judul} pada {tanggal_pinjam.strftime('%Y-%m-%d')}")
        else:
            print(f"Maaf, {buku.judul} sedang tidak tersedia")
    
    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            tanggal_pinjam = self.buku_dipinjam[buku]
            tanggal_kembali = datetime.now()
            selisih_hari = (tanggal_kembali - tanggal_pinjam).days
            
            denda = 0
            if selisih_hari > self.MAKS_HARI_PINJAM:
                denda = (selisih_hari - self.MAKS_HARI_PINJAM) * self.DENDA_PER_HARI
            
            buku.kembalikan()
            del self.buku_dipinjam[buku]
            print(f"{self.nama} telah mengembalikan {buku.judul} pada {tanggal_kembali.strftime('%Y-%m-%d')}.")
            if denda > 0:
                print(f"Terlambat {selisih_hari - self.MAKS_HARI_PINJAM} hari. Denda yang harus dibayar: Rp{denda}")
        else:
            print(f"{self.nama} tidak meminjam buku ini")
    
    def __str__(self):
        return f"{self.nama} (ID: {self.id_anggota})"


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
        self.daftar_anggota = []
    
    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
    
    def daftar_semua_buku(self):
        for buku in self.daftar_buku:
            print(buku)
    
    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)
    
    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None
    
    def buat_laporan(self):
        print("\nLaporan Perpustakaan")
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            print(f"- {buku}")
        print("\nDaftar Anggota dan Buku yang Dipinjam:")
        for anggota in self.daftar_anggota:
            print(f"{anggota.nama}:")
            if anggota.buku_dipinjam:
                for buku, tanggal in anggota.buku_dipinjam.items():
                    print(f"  - {buku.judul} (Dipinjam: {tanggal.strftime('%Y-%m-%d')})")
            else:
                print("  Tidak ada buku yang dipinjam")

# Contoh penggunaan
perpus = Perpustakaan()

# Menambahkan buku
buku1 = Buku(1, "Python untuk Pemula", "John Doe")
buku2 = Buku(2, "Pemrograman Berorientasi Objek", "Jane Doe")
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

# Menambahkan anggota
anggota1 = Anggota(101, "Aziz")
perpus.tambah_anggota(anggota1)

# Menampilkan daftar buku
perpus.daftar_semua_buku()

# Meminjam buku
anggota1.pinjam_buku(buku1)

# Menampilkan daftar buku setelah peminjaman
perpus.daftar_semua_buku()

# Mengembalikan buku setelah beberapa hari (simulasi keterlambatan)
anggota1.kembalikan_buku(buku1)

# Menampilkan laporan perpustakaan
perpus.buat_laporan()
