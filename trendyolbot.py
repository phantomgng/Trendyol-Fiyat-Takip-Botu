import requests
from bs4 import BeautifulSoup
from sendmail import sendMail
import time

# --- Kullanıcıdan Bilgileri Alıyoruz ---
print("--- Gmail Bildirim Ayarları ---")
sender_email = input("Gönderici Gmail adresi: ")
sender_pass = input("Gönderici 16 haneli Uygulama Şifresi: ")
receiver_email = input("Bildirimin gideceği alıcı adresi: ")
target_price = float(input("\nHedef fiyat nedir? (Örn: 77000): "))

url1 = "https://www.trendyol.com/apple/13-macbook-air-apple-m4-chip-with-10-core-cpu-and-10-core-gpu-24gb-512gb-ssd-gumus-p-904728349"

def checkPrice():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
    }
    
    try:
        page = requests.get(url1, headers=headers)
        htmlPage = BeautifulSoup(page.content, "html.parser")
        
        productTitle = htmlPage.find("h1", class_="product-title variant-pdp").get_text(strip=True)
        price_text = htmlPage.find("span", class_="discounted").get_text(strip=True)
        
        # Fiyat temizleme ve dönüştürme
        converted_price = float(price_text.replace("TL", "").replace(".", "").replace(",", ".").strip())
        
        print(f"\n[{time.strftime('%H:%M:%S')}] Ürün: {productTitle}")
        print(f"Güncel Fiyat: {converted_price} TL | Hedef: {target_price} TL")
        
        if converted_price <= target_price:
            print("Fiyat düştü! Mail gönderiliyor...")
            html_content = f"<h2>{productTitle} Fiyatı Düştü!</h2><p><b>{converted_price} TL</b> fiyatıyla yayında.</p><br><a href='{url1}'>Ürünü Satın Al</a>"
            
            # sendMail fonksiyonuna tüm parametreleri gönderiyoruz
            sendMail(sender_email, sender_pass, receiver_email, "Apple Fiyat Alarmı!", html_content)
            return True
        else:
            print("Fiyat henüz düşmedi.")
            return False
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

# --- Sonsuz Döngü ---
print("\nTakip başlatıldı. Programı kapatmak için Ctrl+C tuşlarına basın.")
while True:
    price_reached = checkPrice()
    
    # Fiyat düştüyse ve mail gittiyse durmasını istersen buraya 'break' ekleyebilirsin.
    # Eğer her 10 dakikada bir kontrol etmeye devam etsin dersen dokunma:
    
    time.sleep(600)
