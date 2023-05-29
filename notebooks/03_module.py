import qrcode

data = "Python is great!"
# img = qrcode.make(data)
# img.save("qrcode.png")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")

img.save("qrcode.png")

#decoding the qrcode
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("qrcode.png")
result = decode(img)
print(result)


#new example

import qrcode
from PIL import Image

# Data to be encoded
data = "Hello, World!"

# Instantiate QRCode object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Customize the QR code color and save it
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')

import cv2

# Read the image with OpenCV
img = cv2.imread('qrcode.png')

# Initialize a QRCodeDetector Object
detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, vertices_array, binary_qrcode = detector.detectAndDecode(img)

if vertices_array is not None:
    # Print decoded text
    print(data)
else:
    print("QR code not detected")
