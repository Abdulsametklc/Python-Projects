import kullanici #kullanıcı işlemlerinin bulunduğu modülü ekliyoruz
import yönetici #yöentici işlemlerinin bulunduğu modülü ekliyoruz

def main():
    
    while True:
        print("1.Kullanıcı Girişi")
        print("2.Yönetici Girişi")
        print("0.Çıkış")
        islem = input("Seçiminizi yapın:")
        
        if islem == "1":
            kullanici.kullanici_menu() #ilgili modülden ilgili fonksiyonu çağırıyoruz
            
        elif islem == "2":
            yönetici.yonetici_menu() #ilgili modülden ilgili fonksiyonu çağırıyoruz
            
        elif islem == "0":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Yanlış seçim yaptınız. Lütfen mevcut seçeneklerden birini seçiniz.(1/2/0)")
            
            
if __name__ == "__main__":
    main()