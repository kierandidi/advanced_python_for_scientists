import qrcode
from PIL import Image
import cv2

# Data to be encoded
data = "Hello, World!"
def create_qr_code(data, filename):
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
    img.save(filename + ".png")


def read_qr_code(file):
# Read the image with OpenCV
    img = cv2.imread(file)

    # Initialize a QRCodeDetector Object
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    data, vertices_array, binary_qrcode = detector.detectAndDecode(img)

    if vertices_array is not None:
        return data
    else:
        print("QR code not detected")
