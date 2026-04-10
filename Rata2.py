nama = ["Asep", "Budi", "Cecep"]

nilai = [
    [50, 70, 40, 80],  # Asep
    [78, 78, 80, 65],  # Budi
    [57, 88, 67, 69]   # Cecep
]

rata_mahasiswa = []

for i in range(len(nilai)):
    total = sum(nilai[i])
    rata = total / len(nilai[i])
    rata_mahasiswa.append(rata)

maks = max(rata_mahasiswa)
index_mhs = rata_mahasiswa.index(maks)

rata_mk = []

for j in range(len(nilai[0])): 
    total = 0
    for i in range(len(nilai)):
        total += nilai[i][j]
    rata = total / len(nilai)
    rata_mk.append(rata)

min_mk = min(rata_mk)
index_mk = rata_mk.index(min_mk)

print("Mahasiswa Terpintar :", nama[index_mhs], "(Nilai :", round(maks, 2), ")")
print("Mata Kuliah Nilai Terkecil : MK", index_mk + 1, "(Nilai :", round(min_mk, 2), ")")