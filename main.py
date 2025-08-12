import personel_ekle
import personel_sil
import personel_goster
import personel_maas_degisikligi

def main():
    
    while True:
        
        print("*** İDARİ YÖNETİM SİSTEMİ'NE HOŞGELDİNİZ ***")
        print("1.Personel Ekle")
        print("2.Personel Sil")
        print("3.Personel Maaş Değişikliği")
        print("4.Personelleri Göster")
        print("0.Çıkış")
        islem = input("Yapacağınız işlemi seçiniz:")


        if islem == "1":
            
            personel_ekle.ekle()
            
        elif islem == "2":
            
            personel_sil.sil()
            
        elif islem == "3":
            
            personel_maas_degisikligi.degisiklik()
            
        elif islem == "4":
            
            personel_goster.goster()
            
        elif islem == "0":
            
            print("Programdan çıkış yapılıyor...")
            break
        
        else:
            
            print("Hatalı bir seçim yaptınız. Lütfen tekrar deneyiniz.")
            
if __name__ == "__main__":
    main()