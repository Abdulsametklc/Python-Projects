import whisper 

model = whisper.load_model("base")
result = model.transcribe("ses.mp3", fp16=False, language="tr")

with open("sonuc.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])


#OPENAI WHISPER İLE SES DOSYALARINI YAZIYA DÖKME PROJESİ
''' Bu projeyi kendi bilgisayarınızda çalıştırmak için:
1. OpenAI Whisper kütüphanesini yükleyin: pip install openai-whisper. Torch indirme işlemi sırasında bir hata ile karşıulaşabilirsiniz, bu durumda A. maddesini uygulayın.
2. Ses dosyanızı "ses.mp3" olarak adlandırın ve aynı dizine yerleştirin.
3. Kodunuzu çalıştırın: python main.py. Bu kısımda FFMPEG kütüphanesi kurulu değil ise hata alabilirsiniz, bu durumda B. maddesini uygulayın.
4. Sonuç "sonuc.txt" dosyasına yazılacaktır.
5. Eğer farklı bir dilde transkripsiyon yapmak isterseniz, `language` parametresini değiştirin. Örneğin, İngilizce için `language="en"` kullanabilirsiniz.
'''


# A. Torch İndirme Hatası Çözümü:
'''Windows’ta Long Path desteğini aç

Windows tuşu + R → gpedit.msc yaz ve çalıştır.
(Eğer Windows Home kullanıyorsan Group Policy Editor yoktur, o zaman aşağıdaki Kayıt Defteri (Registry) yöntemini kullan.)

Computer Configuration → Administrative Templates → System → Filesystem yoluna git.

"Enable Win32 long paths" ayarını Enabled yap.

Bilgisayarı yeniden başlat.'''


# B. FFMPEG Kurulumu:
'''ZIP indir -> https://www.gyan.dev/ffmpeg/builds/ → “release essentials” ZIP (adı genelde ffmpeg-*-essentials_build.zip)

Klasöre çıkar
ZIP’i çıkar ve içindeki klasörü C:\ffmpeg konumuna taşı.
Sonunda şu dosya olmalı: C:\ffmpeg\bin\ffmpeg.exe

PATH’e ekle
Başlat → “Ortam değişkenleri” yaz → Sistem ortam değişkenlerini düzenle
Ortam Değişkenleri → Path (Kullanıcı veya Sistem) → Düzenle → Yeni → C:\ffmpeg\bin ekle → Tamam
Yeni bir PowerShell/Komut İstemi aç ve kontrol et: -> ffmpeg -version

Sürüm bilgisi geliyorsa tamamdır.

Sorduğun gibi: PATH’e eklemen gereken tam yol C:\ffmpeg\bin.'''