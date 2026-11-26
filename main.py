# ==========================================================
# Main : menu CLI Aplikasi Rental Kendaraan
# ==========================================================
from mobil import Mobil
from motor import Motor
from pelanggan import Pelanggan
from penyewaan import Penyewaan

# Penyimpanan data sementara
daftar_kendaraan = []
daftar_pelanggan = []
daftar_penyewaan = []

# Fungsi bantu
def input_angka(pesan):
    """Meminta input angka; ulangi sampai valid."""
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")

def cari_kendaraan_by_kode(kode):
    for k in daftar_kendaraan:
        if k.get_kode().lower() == kode.lower():
            return k
    return None

def cari_pelanggan_by_id(id_p):
    for p in daftar_pelanggan:
        if p.get_id().lower() == id_p.lower():
            return p
    return None

def cari_penyewaan_by_id(id_s):
    for s in daftar_penyewaan:
        if s.get_id().lower() == id_s.lower():
            return s
    return None

# Tambah data
def tambah_data():
    print("\n--- TAMBAH DATA ---")
    print("1. Mobil\n2. Motor\n3. Pelanggan\n4. Penyewaan")
    pilih = input("Pilih: ")

    if pilih == "1":
        kode = input("Kode: ")
        if cari_kendaraan_by_kode(kode):
            print("Kode sudah dipakai!"); return
        # Membuat OBJEK Mobil lewat constructor berparameter
        daftar_kendaraan.append(Mobil(kode, input("Merek: "),
                                      input_angka("Harga/hari: "),
                                      input_angka("Jumlah kursi: "),
                                      input("Transmisi (Manual/Matic): ")))
        print("Mobil berhasil ditambahkan.")

    elif pilih == "2":
        kode = input("Kode: ")
        if cari_kendaraan_by_kode(kode):
            print("Kode sudah dipakai!"); return
        daftar_kendaraan.append(Motor(kode, input("Merek: "),
                                      input_angka("Harga/hari: "),
                                      input_angka("Kapasitas CC: "),
                                      input_angka("Jumlah helm: ")))
        print("Motor berhasil ditambahkan.")

    elif pilih == "3":
        id_p = input("ID Pelanggan: ")
        if cari_pelanggan_by_id(id_p):
            print("ID sudah dipakai!"); return
        daftar_pelanggan.append(Pelanggan(id_p, input("Nama: "), input("No HP: ")))
        print("Pelanggan berhasil ditambahkan.")

    elif pilih == "4":
        # Relasi: Penyewaan menghubungkan 1 Pelanggan + 1 Kendaraan
        pelanggan = cari_pelanggan_by_id(input("ID Pelanggan: "))
        kendaraan = cari_kendaraan_by_kode(input("Kode Kendaraan: "))
        if pelanggan is None or kendaraan is None:
            print("Pelanggan atau kendaraan tidak ditemukan!"); return
        if not kendaraan.is_tersedia():
            print("Kendaraan sedang disewa!"); return
        id_s = input("ID Penyewaan: ")
        if cari_penyewaan_by_id(id_s):
            print("ID sudah dipakai!"); return
        lama = input_angka("Lama sewa (hari): ")
        if lama <= 0:
            print("Lama sewa harus lebih dari 0!"); return
        sewa = Penyewaan(id_s, pelanggan, kendaraan, lama)
        daftar_penyewaan.append(sewa)
        print(f"Penyewaan dibuat. Total biaya: Rp{int(sewa.get_total_biaya()):,}")
    else:
        print("Pilihan tidak valid.")

# Tampilkan data
def tampilkan_data():
    print("\n--- TAMPILKAN DATA ---")
    print("1. Kendaraan\n2. Pelanggan\n3. Penyewaan")
    pilih = input("Pilih: ")
    data = {"1": daftar_kendaraan, "2": daftar_pelanggan, "3": daftar_penyewaan}.get(pilih)
    if data is None:
        print("Pilihan tidak valid."); return
    if not data:
        print("Data masih kosong."); return
    for item in data:
        print(item.info())   # polymorphism: info() berbeda tiap class

# Cari data
def cari_data():
    print("\n--- CARI DATA ---")
    print("1. Kendaraan (kode/merek)\n2. Pelanggan (nama)")
    pilih = input("Pilih: ")
    kata = input("Kata kunci: ").lower()
    if pilih == "1":
        hasil = [k for k in daftar_kendaraan
                 if kata in k.get_kode().lower() or kata in k.get_merek().lower()]
    elif pilih == "2":
        hasil = [p for p in daftar_pelanggan if kata in p.get_nama().lower()]
    else:
        print("Pilihan tidak valid."); return
    if not hasil:
        print("Data tidak ditemukan.")
    for h in hasil:
        print(h.info())

# ubah data
def ubah_data():
    print("\n--- UBAH DATA ---")
    print("1. Harga sewa kendaraan\n2. Data pelanggan")
    pilih = input("Pilih: ")
    if pilih == "1":
        k = cari_kendaraan_by_kode(input("Kode kendaraan: "))
        if k is None:
            print("Kendaraan tidak ditemukan."); return
        # Perubahan lewat setter (bukan akses langsung ke atribut private)
        if k.set_harga_per_hari(input_angka("Harga baru/hari: ")):
            print("Harga berhasil diubah.")
        else:
            print("Harga tidak valid (harus > 0).")
    elif pilih == "2":
        p = cari_pelanggan_by_id(input("ID pelanggan: "))
        if p is None:
            print("Pelanggan tidak ditemukan."); return
        p.ubah_data(input("Nama baru (kosongkan jika tetap): "),
                    input("No HP baru (kosongkan jika tetap): "))
        print("Data pelanggan berhasil diubah.")
    else:
        print("Pilihan tidak valid.")

# Cek status
def cek_status():
    print("\n--- CEK STATUS ---")
    print("1. Status kendaraan\n2. Status penyewaan / selesaikan sewa")
    pilih = input("Pilih: ")
    if pilih == "1":
        k = cari_kendaraan_by_kode(input("Kode kendaraan: "))
        print(f"Status {k.get_merek()}: {k.get_status()}" if k else "Tidak ditemukan.")
    elif pilih == "2":
        s = cari_penyewaan_by_id(input("ID penyewaan: "))
        if s is None:
            print("Penyewaan tidak ditemukan."); return
        print(s.info())
        if not s.is_selesai() and input("Selesaikan sewa? (y/n): ").lower() == "y":
            s.selesaikan()
            print("Sewa selesai, kendaraan sudah dikembalikan.")
    else:
        print("Pilihan tidak valid.")

# Data
def isi_data_awal():
    daftar_kendaraan.append(Mobil("M01", "Toyota Avanza", 350000, 7, "Manual"))
    daftar_kendaraan.append(Motor("T01", "Honda Vario", 100000, 150, 2))
    daftar_pelanggan.append(Pelanggan("P01", "Budi Santoso", "081234567890"))

# Main utama
def main():
    isi_data_awal()
    while True:
        print("\n===== RENTAL KENDARAAN =====")
        print("1. Tambah Data\n2. Tampilkan Data\n3. Cari Data")
        print("4. Ubah Data\n5. Cek Status Data\n6. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1": tambah_data()
        elif pilih == "2": tampilkan_data()
        elif pilih == "3": cari_data()
        elif pilih == "4": ubah_data()
        elif pilih == "5": cek_status()
        elif pilih == "6":
            print("Terima kasih!"); break
        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()