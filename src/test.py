
import qrcode_utils

# Create a "classic" QR code
qrcode_utils.create_qr_code('https://www.twitter.com', 'twitter')

print(qrcode_utils.data)

# from qr_star import build_qr
# dir(build_qr)
# build_qr.create_dark_qr_code('https://www.twitter.com', 'twitter')