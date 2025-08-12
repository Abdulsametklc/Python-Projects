def sil():
    sil=input("Silinecek personelin ID'sini giriniz:")
    kisi_bulundu = False
    
    if not len(sil) == 6:
        print("Lütfen ID numarasını 6 haneli olacak şekilde giriniz.")
        
        
    else: 
        with open("bilgiler.txt", "r", encoding = "utf-8") as file:
            satirlar = file.readlines()
        
        with open ("bilgiler.txt", "w", encoding ="utf-8") as file:
            for satir in satirlar:
                if sil not in satir:
                    file.write(satir)
                else:
                    kisi_bulundu = True
                
            if kisi_bulundu:
                print(f"{sil} ID numaralı personel listeden silinmiştir.")
                
                
            else: 
                print("Aradığınız ID numarasına sahip personel bulunmamaktadır.")                
        
        