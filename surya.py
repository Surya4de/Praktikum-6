data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir
    })

    tambah = input("\nTambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

print("=" * 64)
print(f"{'No':<4}{'Nama':<15}{'NIM':<10}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Akhir':<10}")
print("=" * 64)

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i:<4}{mahasiswa['nama']:<15}{mahasiswa['nim']:<10}{mahasiswa['tugas']:<10}"
          f"{mahasiswa['uts']:<10}{mahasiswa['uas']:<10}{mahasiswa['akhir']:<10.2f}")

print("=" * 64)
