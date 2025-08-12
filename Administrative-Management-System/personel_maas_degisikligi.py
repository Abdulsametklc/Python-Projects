def degisiklik():
    kod = input("Maaş değişikliği yapacağınız personelin ID numarasını giriniz:")
    yeni_maas = input("Yeni maaşı giriniz: ")
    kisi_bulundu= False
    
    if len(kod) !=6:
        print("Lütfen 6 haneli ID numarasını doğru bir biçimde giriniz.")
        
    else:
        
        with open("bilgiler.txt","r", encoding =" utf-8") as file :
            satirlar = file.readlines()
                    
        with open("bilgiler.txt", "w", encoding ="utf-8") as file:
            for satir in satirlar:
                if f"ID: {kod}" in satir: #ID'yi bulup, maaş bilgisine yeni maaş bilgisini atıyoruz.
                    parcalar = satir.split(", ")
                    parcalar[4] = f"Maaş: {yeni_maas}"
                    file.write(", ".join(parcalar)) #
                    kisi_bulundu = True 
                else:
                    file.write(satir)   
                                   
                                   
        if kisi_bulundu:                                        
                print(f"{kod} ID numaralı personelin yeni maaş ücreti {yeni_maas} olarak güncellenmiştir.")
                    
        else:
                print(f"{kod} ID numarasına sahip personel bulunmadı. Tekrar deneyiniz.")