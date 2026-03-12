import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(senderMail, senderPassword, toMail, subject, content):
    try:
        # Sunucu Bağlantısı
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        # Kullanıcıdan gelen bilgilerle giriş
        server.login(senderMail, senderPassword)
        
        # Mesaj Oluşturma
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = senderMail
        message["To"] = toMail
        
        # İçeriği UTF-8 olarak ekle (Türkçe karakter sorunu olmaması için)
        message.attach(MIMEText(content, "html", "utf-8"))
        
        # Gönderim
        server.sendmail(senderMail, toMail, message.as_string())
        server.quit()
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"Mail gönderilirken bir hata oluştu: {e}")
