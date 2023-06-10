from qr_star.utils_qr import create_qr_code, read_qr_code
import qrcode

# Create a "classic" QR code

def create_classic_qr_code(data, filename):
    create_qr_code(data, filename, version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_L, 
                   box_size=10, border=4, fill_color="black", back_color="white")
    
def create_dark_qr_code(data, filename):
    create_qr_code(data, filename, version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_L, 
                   box_size=10, border=4, fill_color="white", back_color="grey")
    
def create_colorful_qr_code(data, filename):
    create_qr_code(data, filename, version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_L, 
                   box_size=10, border=4, fill_color="red", back_color="yellow")