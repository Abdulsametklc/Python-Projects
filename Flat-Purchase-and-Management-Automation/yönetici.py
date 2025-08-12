import main #main.py modülünü ekleyerek ilk menüye dönüşü sağlıyoruz
def yonetici_menu():
    
    yonetici_bilgileri = {
        "Abdulsamet": "145320",
        "Betul": "147852",
        "Mete": "123456"
    } #Yönetici bloğuna girmek isteyenlerin kullanıcı adı ve şifrelerinin bulunduğu kısımdır. Buraya belirtilen formatta ekleme ve çıkarma yapılarak kullanıcı adı ve şifreler değiştirilebilir.
    
    giris_yapildi = False
    
    while not giris_yapildi: 
        girilen_kullanici = input("Kullanıcı Adı: ")
        girilen_sifre = input("Şifre: ")
        
        if girilen_kullanici in yonetici_bilgileri and girilen_sifre == yonetici_bilgileri[girilen_kullanici]:
            giris_yapildi =True # Eğer ki bilgiler doğru ise " giris_yapildi" değişeni true olacak, while koşulundan çıkacak ve sisteme giriş sağlayacağız.
        else:
            print("Hatalı kullanıcı adı ve şifre. Lütfen tekrar deneyiniz.")
            # Yanlış ise devam_et değişkeni ile kullanıcının sisteme giriş yapıp yapmayacağını sorguluyoruz.
            devam_et = input("Menüye geri dönmek için 'q', tekrar giriş yapmak için 'm' tuşunua basın: ")
            if devam_et == 'q':
                return
        
    while True:    
        print("1.Ev Ekle")
        print("2.Ev Sil")
        print("3.Evleri Görüntüle")
        print("4.İlk Menüye Geri Dön")
        secim = input("Seçim yapınız:")
        
        if secim == "1":
            sehir_ekle = input("Şehir: ")
            oda_ekle = input("Oda: ")
            fiyat_ekle = input("Fiyat: ")
            kod_ekle = input("Kod: ") # input değerlerini değişkenlere atıyoruz.
           
            with open("ev_listesi.txt","r", encoding ="utf-8") as file:
                satirlar = file.readlines()
                for satir in satirlar:
                    if "Kodu: " + kod_ekle in satir:
                        print(f"{kod_ekle} numaralı kod zaten var.")
                        break # ev_listesi.txt dosyasını okuyoruz ve yeni eklenecek eve verilecek kod sistemde var ise uyarı mesajı karşılaşıyoruz. 
                else:
                    with open("ev_listesi.txt","a", encoding ="utf-8") as file:      
                        file.write("Şehir: "+ sehir_ekle+ ", "+"Oda Türü: "+ oda_ekle+ ", "+"Fiyatı: "+ fiyat_ekle+ ", "+"Kodu: "+ kod_ekle+ "\n")
                        print(f"Yeni {kod_ekle} numaralı daire listeye eklendi.") #Bilgiler doğru ise txt dosyasına bilgiler ekleniyor.
            
              
        elif secim == "2":
            kod = int(input("Silmek istediğiniz evin kodunu giriniz:"))

            with open('ev_listesi.txt', 'r', encoding="utf-8") as file:
                satirlar = file.readlines()

                ev_bulundu = False

            with open('ev_listesi.txt', 'w', encoding="utf-8") as file:
                for satir in satirlar:
                    if str(kod) not in satir:
                        file.write(satir)
                    else:
                        ev_bulundu = True # Ev silme işleminde verilen satır verisi kod bilgisi ile aranıyor. Eğer ki kod geçerli ise o verinin bulunduğu satırı atlayarak okunann verileri tekrar txt dosyasına ekliyoruz. Bu sayede silmek istediğimiz veriyi listeden kaldırmış oluyoruz.

            if ev_bulundu:
                print(f"{kod} numaralı daire listeden silindi.")
            else:
                print("Yanlış kod verdiniz. Bu kodla eşleşen bir daire bulunamadı.")
                
            
                
        elif secim == "3":
            with open("ev_listesi.txt","r", encoding ="utf-8") as file:
                for sirala in file:
                    print(sirala)
        # Listeyi dosya işlemlerinin "r" kipi kullanarak kullanıcıya gösterilmesini sağlıyoruz.                    
        elif secim == "4":
            main.main() # İlk menüye dönüşünü sağlıyoruz.
                    
        else:
            print("Yanlış seçim yaptınız. Tekrar deneyiniz.")