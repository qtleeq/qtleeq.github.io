import qrcode

data = "qtleeq.github.io"

img = qrcode.make(data)

img.save("vvb_qrcode.png")
