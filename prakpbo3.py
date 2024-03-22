class Praktikan:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def get_fakultas(self):
        return self.fakultas

    def get_hobi(self):
        return self.hobi

# Membuat object praktikan
praktikan = Praktikan("Zahwa Nur Azkia Putri", "064002300038", "Fakultas Teknik Informatika", "Tidur")

# Menampilkan informasi praktikan
print("---PROGRAM MENAMPILKAN IDENTITAS---")
print("Nama saya adalah ", praktikan.get_nama())
print("NIM saya ", praktikan.get_nim())
print("Saya dari Fakultas ", praktikan.get_fakultas())
print("Hobi saya adalah ", praktikan.get_hobi())
