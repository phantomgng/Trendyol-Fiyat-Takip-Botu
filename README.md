🚀 Trendyol Fiyat Takip Botu (MacBook Air M4)
Bu Python projesi, Trendyol üzerindeki belirli bir ürünün (MacBook Air M4) fiyatını otomatik olarak takip eder ve fiyat belirlediğiniz limitin altına düştüğünde size anlık e-posta bildirimi gönderir.

✨ Özellikler
Anlık Takip: Belirlenen süre aralıklarıyla (varsayılan 10 dakika) fiyatı kontrol eder.

Akıllı Bildirim: Sadece fiyat hedeflediğiniz rakama ulaştığında mail gönderir.

Güvenli Tasarım: Kişisel verilerinizi kodun içinde tutmaz, kullanıcıdan çalışma anında talep eder.

HTML E-posta: Şık bir e-posta formatı ile ürün başlığını ve yeni fiyatı iletir.

🛠️ Kurulum
Depoyu Klonlayın:

Bash
git clone https://github.com/kullaniciadin/trendyol-fiyat-takip.git
cd trendyol-fiyat-takip
Gerekli Kütüphaneleri Yükleyin:

Bash
pip install requests beautifulsoup4
Gmail Uygulama Şifresi Alın:

Google hesabınızda "İki Adımlı Doğrulama"yı açın.

Uygulama Şifreleri kısmından Python botunuz için 16 haneli bir kod oluşturun.

🚀 Kullanım
Programı başlatmak için terminale şu komutu yazın:

Bash
python trendyolbot.py
Program başladığında sizden şu bilgileri isteyecektir:

Gönderici Mail: Bildirimi gönderecek Gmail adresi.

Uygulama Şifresi: Google'dan aldığınız 16 haneli kod.

Alıcı Mail: Bildirimi almak istediğiniz adres.

Hedef Fiyat: Hangi fiyatın altında mail gelmesini istiyorsunuz?

📂 Dosya Yapısı
trendyolbot.py: Ana döngünün çalıştığı ve web kazıma (scraping) işlemlerinin yapıldığı dosya.

sendmail.py: SMTP protokolü ile mail gönderimini sağlayan yardımcı modül.

.gitignore: Hassas bilgilerin ve gereksiz dosyaların GitHub'a yüklenmesini engeller.

⚠️ Önemli Notlar
User-Agent: Web sitelerinin botları engellemesini önlemek için kodda güncel bir User-Agent kullanılmıştır.

Zaman Aralığı: time.sleep(600) komutu Trendyol sunucularını yormamak ve IP engelinden kaçınmak için 10 dakikaya ayarlanmıştır.

📝 Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Dilediğiniz gibi geliştirebilir ve kullanabilirsiniz.
