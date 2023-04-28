# python-projects
import qrcode as qr
image = qr.make("https://www.youtube.com/channel/UCCK8jN50-3idCqMQPhR6E0Q")
image.save("Chiranjeevi Vaston_youtube channel.png")


this is program to create simple the QR code. by the help of that ppython program

Qr.make("Enter the link or any that you wanna to show ")
image.save ("here the Enter the name of the pic to understand the people ") 





# mofificated QRcode generator 
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

here we have to create the modificated QRCODE 
first import the QRCODE module
qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=4)
                    # this using to clear errors box size set border set
image = qr.make_image(fill_color="red",back_color="blue")
it is used to color of the qr code and background color.
