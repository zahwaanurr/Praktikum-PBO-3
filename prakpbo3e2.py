class Praktikan:
    def __init__(self, nama, nim, fakultas):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def get_fakultas(self):
        return self.fakultas


class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def get_panjang(self):
        return self.panjang

    def get_lebar(self):
        return self.lebar


nama = "Zahwa Nur Azkia Putri"
nim = "064002300038"
fakultas = "Teknik Informatika"

praktikan = Praktikan(nama, nim, fakultas)

print(praktikan.get_nama())
print(praktikan.get_nim())
print(praktikan.get_fakultas())

persegi_panjang1 = PersegiPanjang(20, 12)

print("\n---PROGRAM MENGHITUNG LUAS PERSEGI PANJANG---")
print("Persegi Panjang dengan panjang", persegi_panjang1.get_panjang(), "dan lebar", persegi_panjang1.get_lebar(), "memiliki luas sebesar", persegi_panjang1.luas())
