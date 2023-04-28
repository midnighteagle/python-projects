import qrcode
import qrcode.constants
from PIL import Image
qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=4)
qr.add_data("xnxx.com")
qr.make(fit=True)
image = qr.make_image(fill_color="red",back_color="blue")
image.save("porn_web.png")
