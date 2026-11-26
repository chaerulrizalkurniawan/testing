# ==========================================================
# Subclass Mobil (extends Kendaraan)
# ==========================================================
from kendaraan import Kendaraan


class Mobil(Kendaraan):
  

    def __init__(self, kode, merek, harga_per_hari, jumlah_kursi, transmisi):
        # Memanggil constructor superclass
        super().__init__(kode, merek, harga_per_hari)
        # Atribut private milik Mobil
        self.__jumlah_kursi = jumlah_kursi
        self.__transmisi = transmisi  # "Manual" / "Matic"

    # Getter
    def get_jumlah_kursi(self):
        return self.__jumlah_kursi

    def get_transmisi(self):
        return self.__transmisi

    # Method tambahan
    def hitung_asuransi(self, lama_hari):
        """Asuransi mobil: Rp25.000 per hari."""
        return 25000 * lama_hari

    # Override: biaya mobil = biaya dasar + asuransi
    def hitung_biaya(self, lama_hari):
        return super().hitung_biaya(lama_hari) + self.hitung_asuransi(lama_hari)

    # Override: tampilkan info tambahan mobil
    def info(self):
        return (f"MOBIL | {super().info()} | "
                f"{self.__jumlah_kursi} kursi | {self.__transmisi}")
