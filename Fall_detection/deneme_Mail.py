import smtplib

content = "Pillover bir dusme olayi tespit ettigi icin size bu e-postayi gonderdi. Lutfen yakininizla iletisime gecip durumunu kontrol edin."

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('gonderen_e_posta', 'gonderen_e_posta_sifre')

mail.sendmail('kucar17@gmail.com', 'kucar17@gmail.com', content)

print("E-mail gönderildi!")

mail.close()