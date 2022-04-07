import qrcode

qr = qrcode.QRCode(version = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=5)

giden_deger = "https://www.linkedin.com/in/kursatkeskin06/"

qr.add_data(giden_deger)
qr.make(fit=True)

resim = qr.make_image(fill_color = "black",back_color = "white")
resim.save("Linkedin.png")
