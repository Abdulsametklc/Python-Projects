def kullanici_menu():
    hangi_sehir = input("Hangi şehirde ev satın almak istersiniz?")
    kac_odali = input("Kaç odalı olmasını istersiniz?")
    min_fiyat = float(input("Minimum fiyat bütçenizi belirtir misiniz?"))
    max_fiyat = float(input("Maksimum fiyat bütçenizi belirtir misiniz?"))

    veriler = []
    with open("ev_listesi.txt", "r", encoding="utf-8") as dosya:
        for satir in dosya:
            veriler.append(satir.strip()) # Listemiz içindeki verileri okuyarak gereksiz bozuklukları temizleyip, verileri veriler[] listesine atıyoruz.
    
    uygun_daireler = []
    for veri in veriler:
        if hangi_sehir in veri and kac_odali in veri:
            fiyat_str = veri.split("Fiyatı: ")[1].split(",")[0].replace(" TL", "").replace(",", "")
            try:
                fiyat = float(fiyat_str)
                if min_fiyat <= fiyat <= max_fiyat:
                    uygun_daireler.append(veri) # Kullanıcın istediği bilgileri alarak, filtreleme işlemi yapıyoruz.
            except ValueError: # Oluşacak dönüşüm hatasında program except ValueError bloğuna girip ve hatayı görmezden gelerek işlemine devam eder.
                continue
    if not uygun_daireler:
        print("Üzgünüz, istediğniz özelliklere uygun daire bulunamadı.")
        return # İstenilen özelliklerde daire bulunmazsa uyarı mesajı ile menüye geri dönüş yapıyoruz.
    
    print("Size uygun daireler:")
    for daire in uygun_daireler:
        print(daire) # İstenilen özelliklere sahip daireler kullanıcıya sunuluyor.
        
    while True:    
        satın_alma_islemi = input("Listeden satın alma işlemi gerçekleştirecek misiniz?")
        if satın_alma_islemi.lower() == "hayır":# lower() fonskiyonu ile yazı formatı sıkıntısını engelliyoruz. EVET, evet vb. cevapları geçerli saymamıza yarıyor.
            print("İyi Günler!")
            break 
        elif satın_alma_islemi.lower() != "evet":
            print("Lütfen geçerli bir seçenek giriniz (Evet/Hayır).")
        else: 
            satın_alma_kodu_str = input("Almak istediğiniz evin 4 basamaklı kodunu giriniz:")
            if not satın_alma_kodu_str.isdigit() or len(satın_alma_kodu_str) != 4: # Girilen kod 4 basamaktan fazla veya az ise uyarı mesajı veriyoruz. Tekrardan kodu girmesini istiyoruz.
                #isdigit() metodu ile girilen değerin sayısal olup olmadığını kontrol ediyoruz.
                print("Geçerli bir kod girmediniz. Lütfen 4 basamaklı bir sayı girin.")
            else:
                satın_alma_kodu = int(satın_alma_kodu_str)
                ev_bulundu = False
    
                with open('ev_listesi.txt', 'r', encoding="utf-8") as file:
                    satirlar = file.readlines()

                with open('ev_listesi.txt', 'w', encoding="utf-8") as file:
                    for satir in satirlar:
                        if str(satın_alma_kodu) not in satir:
                            file.write(satir)  #Eğer girilen 4 basamaklı kod için ev bulunmamakta ise false değerli ile if-else koşulunda gerekli mesajları veriyoruz.
                        else:
                            ev_bulundu = True
                if ev_bulundu:
                    print(f"{satın_alma_kodu}'lu evi başarılı bir şekilde satın aldınız.")
                    break
                else:
                    print(f"{satın_alma_kodu}'lu ev bulunmamaktadır. Lütfen tekrar deneyiniz.")
            
        
if __name__ == "__main__":
    kullanici_menu()
