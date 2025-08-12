from ucus import Ucus
from yolcu import Yolcu

def main():
    ucus_listesi = []

    while True:
        print("\n*** UÇUŞ TAKİP SİSTEMİ ***")
        print("1. Yeni Uçuş Oluştur")
        print("2. Yolcu Ekle")
        print("3. Yolcu Sil")
        print("4. Uçuş Bilgilerini Görüntüle")
        print("0. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            ucus_numarasi = input("Uçuş Numarası: ")
            kalkis_yeri = input("Kalkış Yeri: ")
            varis_yeri = input("Varış Yeri: ")
            kalkis_tarihi = input("Kalkış Tarihi: ")
            varis_tarihi = input("Varış Tarihi: ")
            ucus = Ucus(ucus_numarasi, kalkis_yeri, varis_yeri, kalkis_tarihi, varis_tarihi)
            ucus_listesi.append(ucus)
            print("Yeni uçuş oluşturuldu.")
        elif choice == "2":
            if not ucus_listesi:
                print("Önce bir uçuş oluşturmalısınız.")
                continue
            ucus_numarasi = input("Yolcu eklemek istediğiniz uçuşun numarasını girin: ")
            ucus = None
            for ucus_obj in ucus_listesi:
                if ucus_obj.ucus_numarasi == ucus_numarasi:
                    ucus = ucus_obj
                    break
            if not ucus:
                print("Belirtilen uçuş numarası bulunamadı.")
                continue
            ad = input("Yolcu Adı: ")
            soyad = input("Yolcu Soyadı: ")
            koltuk_numarasi = input("Yolcu Koltuk Numarası: ")
            yolcu = Yolcu(ad, soyad, koltuk_numarasi)
            ucus.yolcu_ekle(yolcu)
            print("Yolcu eklendi.")
        elif choice == "3":
            if not ucus_listesi:
                print("Önce bir uçuş oluşturmalısınız.")
                continue
            ucus_numarasi = input("Yolcu silmek istediğiniz uçuşun numarasını girin: ")
            ucus = None
            for ucus_obj in ucus_listesi:
                if ucus_obj.ucus_numarasi == ucus_numarasi:
                    ucus = ucus_obj
                    break
            if not ucus:
                print("Belirtilen uçuş numarası bulunamadı.")
                continue
            ad = input("Silmek istediğiniz yolcunun adını girin: ")
            soyad = input("Silmek istediğiniz yolcunun soyadını girin: ")
            for yolcu in ucus.yolcular:
                if yolcu.ad == ad and yolcu.soyad == soyad:
                    ucus.yolcu_sil(yolcu)
                    print("Yolcu silindi.")
                    break
            else:
                print("Belirtilen yolcu bulunamadı.")
        elif choice == "4":
            if not ucus_listesi:
                print("Önce bir uçuş oluşturmalısınız.")
                continue
            ucus_numarasi = input("Bilgilerini görmek istediğiniz uçuşun numarasını girin: ")
            ucus = None
            for ucus_obj in ucus_listesi:
                if ucus_obj.ucus_numarasi == ucus_numarasi:
                    ucus = ucus_obj
                    break
            if not ucus:
                print("Belirtilen uçuş numarası bulunamadı.")
                continue
            ucus.bilgileri_goruntule()
        elif choice == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
