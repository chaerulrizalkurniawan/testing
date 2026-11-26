# ==========================================================
# Superclass Kendaraan (induk dari Mobil dan Motor)
# ==========================================================

class Kendaraan:

    # Constructor berparameter
    def __init__(self, kode, merek, harga_per_hari):
        # Atribut private (diawali dua underscore)
        self.__kode = kode
        self.__merek = merek
        self.__harga_per_hari = harga_per_hari
        self.__tersedia = True  # True = bisa disewa, False = sedang disewa

    # Akses baca atribut private
    def get_kode(self):
        return self.__kode

    def get_merek(self):
        return self.__merek

    def get_harga_per_hari(self):
        return self.__harga_per_hari

    def is_tersedia(self):
        return self.__tersedia

    # Akses ubah dengan validasi
    def set_harga_per_hari(self, harga_baru):
        # Validasi agar harga tidak boleh negatif/nol
        if harga_baru > 0:
            self.__harga_per_hari = harga_baru
            return True
        return False

     # Mengubah status kendaraan menjadi sedang disewa
    def sewa(self):
      
        if self.__tersedia:
            self.__tersedia = False
            return True
        return False

    # Mengubah status kendaraan menjadi tersedia lagi
    def kembalikan(self):

        self.__tersedia = True

    # Mengecek status
    def get_status(self):
        return "Tersedia" if self.__tersedia else "Sedang Disewa"

    # Menghitung biaya
    def hitung_biaya(self, lama_hari):
      
        return self.__harga_per_hari * lama_hari

    # Menampilkan informasi dasar kendaraan
    def info(self):
        
        return (f"[{self.__kode}] {self.__merek} | "
                f"Rp{self.__harga_per_hari:,}/hari | {self.get_status()}")