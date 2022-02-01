import qrcode
import qrcode.image.svg
img = qrcode.make('https://ea17-ai.github.io/cv/', image_factory=qrcode.image.svg.SvgImage)
with open('qr.svg', 'wb') as qr:
    img.save(qr)
