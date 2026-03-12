import requests
from bs4 import BeautifulSoup
from sendmail import sendMail
import time

# Kullanıcıdan bilgileri alıyoruz
user_email = input("Hangi e-posta adresine bildirim gitsin? (Örn: example@gmail.com): ")
target_price = float(input("Fiyat kaça (veya altına) düşerse haber vereyim? (Örn: 77000): "))

url1 = "https://www.trendyol.com/apple/13-macbook-air-apple-m4-chip-with-10-core-cpu-and-10-core-gpu-24gb-512gb-ssd-gumus-p-904728349"

def checkPrice():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
    }
    
    try:
        page = requests.get(url1, headers=headers)
        htmlPage = BeautifulSoup(page.content, "html.parser")
        
        # Ürün başlığı ve fiyatı çekiliyor
        productTitle = htmlPage.find("h1", class_="product-title variant-pdp").get_text(strip=True)
        price_text = htmlPage.find("span", class_="discounted").get_text(strip=True)
        
        # Fiyatı sayıya çevirme işlemi
        converted_price = float(price_text.replace("TL", "").replace(".", "").replace(",", ".").strip())
        
        print(f"Kontrol edildi: {productTitle} - Şu anki Fiyat: {converted_price} TL")
        
        if converted_price <= target_price:
            print("Hedef fiyata ulaşıldı! E-posta gönderiliyor...")
            html_content = f"<h1>{productTitle} Fiyatı Düştü!</h1><p>Yeni fiyat: <b>{converted_price} TL</b></p><br><a href='{url1}'>Ürüne Git</a>"
            sendMail(user_email, "MacBook Air Fiyatı Düştü!", html_content)
            return True # Mail gönderildiğinde döngüyü durdurmak istersen kullanabilirsin
        else:
            print(f"Fiyat henüz düşmedi. Hedefin: {target_price} TL")
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Sonsuz Döngü
while True:
    checkPrice()
    print("10 dakika sonra tekrar kontrol edilecek...")
    # 10 dakika = 600 saniye (Trendyol'un seni engellememesi için daha güvenli)
    time.sleep(600)
