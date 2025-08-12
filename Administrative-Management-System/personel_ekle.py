import main
def ekle():
    
 while True: 
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    tc = input("TC Kimlik Numarası: ")
    brans = input("Branş: ")
    maas = input("Maaş: ")
    telefon = input("Telefon Numarası: ")
    id = input("ID(Örnek: aa77aa formatında ID ekleyiniz.): ")
    
    if giris_uzunlugu_dogrula(tc, 11) and giris_uzunlugu_dogrula(telefon, 11) and giris_uzunlugu_dogrula(id, 6): #oluşturduğum karakter doğrulama fonksiyonu ile tc, ıd ve telefon numaralarını kontrol ediyorum.
        with open("bilgiler.txt", "r", encoding = "utf-8") as file:
            satirlar = file.readlines()
            for satir in satirlar:
                if "ID: " + str(id) in satir:
                    print(f"{id} ID sistemde farklı bir personele atanmıştır. Lütfen yeni bir ID giriniz.")
                    break
                    
            else:
                        
                with open ("bilgiler.txt", "a", encoding = "utf-8") as file:
                    file.write("İsim: " + isim + ", " + "Soyisim: " + soyisim + ", " + "TC: " + tc + ", " + "Branş: " + brans + ", " + "Maaş: " + maas + ", " + "Telefon Numarası: " + telefon + ", " + "ID: " + id + "\n")
                    print(f"{isim} {soyisim} sisteme {id} id ile eklendi. ")
            main.main()
        
    else:
        print("TC, telefon numarası veya ID numarasını hatalı girdiniz. Lütfen tekrar deneyiniz.")
        
                    
                    
                    
def giris_uzunlugu_dogrula(girdi, uzunluk):
    return len(girdi) == uzunluk
    