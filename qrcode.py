import segno
url = "https://yushangchenintern.vercel.app/"
qrcode = segno.make_qr(url)
qrcode.save("basic_qrcode.png")