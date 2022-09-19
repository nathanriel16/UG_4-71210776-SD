import json

with open('mahasiswa.json', 'r') as datafile:
    data = []
    jummahasiswa = int(input("Masukan jumlah mahasiswa baru :"))

    for i in range(0, jummahasiswa):
        nama = input("Masukan nama Anda :")
        listt = []
        dctry = {}
        jml_hobi = int(input("Masukan Jumlah hobi :"))
        listt_hobi = []
        for j in range(1, jml_hobi+1):
            hobi = input("Masukan Hobi ke-{index} :".format(index=j))
            listt_hobi.append(hobi)
        prestasi = input("Masukan Prestasi Anda :")

        listt.append({"BioData":{"Hobi":listt_hobi,"Prestasi":prestasi}})
        data[nama] = str(listt)


        print("=== Data berhasil ditambahkan ===")
        print()

with open('mahasiswa.json', 'w') as datafile:
    json.dump(data, datafile)