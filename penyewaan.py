# ==========================================================
# penyewaan.py
# Class relasi (Association): Penyewaan memiliki
# SATU Pelanggan dan SATU Kendaraan
# ==========================================================

class Penyewaan:
    def __init__(self, id_sewa, pelanggan, kendaraan, lama_hari):
        # Atribut private; pelanggan & kendaraan adalah OBJEK (relasi)
        self.__id_sewa = id_sewa
        self.__pelanggan = pelanggan      # objek Pelanggan
        self.__kendaraan = kendaraan      # objek Kendaraan / Mobil / Motor
        self.__lama_hari = lama_hari
        self.__selesai = False
        # Total biaya dihitung via polymorphism (Mobil/Motor beda cara hitung)
        self.__total_biaya = kendaraan.hitung_biaya(lama_hari)
        # Kendaraan otomatis berstatus "Sedang Disewa"
        kendaraan.sewa()

    # Getter
    def get_id(self):
        return self.__id_sewa

    def get_pelanggan(self):
        return self.__pelanggan

    def get_kendaraan(self):
        return self.__kendaraan

    def get_total_biaya(self):
        return self.__total_biaya

    def is_selesai(self):
        return self.__selesai

    # Method tambahan
    def selesaikan(self):
        """Menandai sewa selesai dan mengembalikan kendaraan."""
        if not self.__selesai:
            self.__selesai = True
            self.__kendaraan.kembalikan()
            return True
        return False

    def get_status(self):
        return "Selesai" if self.__selesai else "Berjalan"

    def info(self):
        return (f"[{self.__id_sewa}] {self.__pelanggan.get_nama()} menyewa "
                f"{self.__kendaraan.get_merek()} selama {self.__lama_hari} hari | "
                f"Total: Rp{int(self.__total_biaya):,} | {self.get_status()}")