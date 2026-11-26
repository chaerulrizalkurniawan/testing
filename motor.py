# ==========================================================
# motor.py
# Subclass Motor (extends Kendaraan)
# ==========================================================
from kendaraan import Kendaraan


class Motor(Kendaraan):
    """Subclass: kendaraan jenis motor."""

    def __init__(self, kode, merek, harga_per_hari, kapasitas_cc, jumlah_helm):
        # Memanggil constructor superclass
        super().__init__(kode, merek, harga_per_hari)
        # Atribut private milik Motor
        self.__kapasitas_cc = kapasitas_cc
        self.__jumlah_helm = jumlah_helm

    # Getter
    def get_kapasitas_cc(self):
        return self.__kapasitas_cc

    def get_jumlah_helm(self):
        return self.__jumlah_helm

    # Method tambahan
    def hitung_diskon(self, lama_hari):
        """Diskon 10% jika sewa 3 hari atau lebih."""
        if lama_hari >= 3:
            return super().hitung_biaya(lama_hari) * 0.10
        return 0

    # Override: biaya motor = biaya dasar - diskon
    def hitung_biaya(self, lama_hari):
        return super().hitung_biaya(lama_hari) - self.hitung_diskon(lama_hari)

    # Override: tampilkan info tambahan motor
    def info(self):
        return (f"MOTOR | {super().info()} | "
                f"{self.__kapasitas_cc}cc | {self.__jumlah_helm} helm")