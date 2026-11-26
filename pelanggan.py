# ==========================================================
# pelanggan.py
# Class Pelanggan (penyewa kendaraan)
# ==========================================================

class Pelanggan:
    def __init__(self, id_pelanggan, nama, no_hp):
        # Atribut private
        self.__id_pelanggan = id_pelanggan
        self.__nama = nama
        self.__no_hp = no_hp

    # Getter
    def get_id(self):
        return self.__id_pelanggan

    def get_nama(self):
        return self.__nama

    def get_no_hp(self):
        return self.__no_hp

    # Method tambahan (setter dengan validasi)
    def ubah_data(self, nama_baru, no_hp_baru):
        """Mengubah nama / no HP. Kosongkan input untuk tidak mengubah."""
        if nama_baru:
            self.__nama = nama_baru
        if no_hp_baru:
            self.__no_hp = no_hp_baru

    def info(self):
        return f"[{self.__id_pelanggan}] {self.__nama} | HP: {self.__no_hp}"