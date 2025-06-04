class Anbar:
    def __init__(self):
        self.mehsullar = dict()
    def mehsul_elave_et(self, name, count):
        if name in self.mehsullar:
            self.mehsullar[name] += count
        self.mehsullar[name] = count
        print(f"{name} Birlab anbarina daxil oldu")
    def mehsul_sil(self, name):
        if name in self.mehsullar:
            self.mehsullar.pop(name)
            print(f"{name} anbardan silindi.")
        else:
            print(f"{name} anbarda tapılmadı.")
    def mehsullari_goster(self):
        if self.mehsullar:
            print("Anbardakı mehsullar:")
            for i in self.mehsullar:
                print(f"---{i}-{self.mehsullar[i]}")
        else:
            print("Anbar boşdur.")
anbar = Anbar()
while True:
    print("\n--- ANBAR IDAREETME MENYUSU ---")
    print("1. Mehsul elave et")
    print("2. Mehsul sil")
    print("3. Mehsullara bax")
    print("4. Çıxış")
    secim = input("Seçim et: ")
    match secim:
        case "1":
            mehsul = input("Mehsulun adi: ")
            anbar.mehsul_elave_et(mehsul)
        case "2":
            mehsul = input("Silinecek mehsul: ")
            anbar.mehsul_sil(mehsul)
        case "3":
            anbar.mehsullari_goster()
        case "4":
            print("Proqramdan çıxılır...")
            break
        case _:
            print("Yanlış seçim!")