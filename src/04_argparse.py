import argparse
from qr_star.utils_qr import create_qr_code
import qrcode

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR codes with various styles.")
    
    parser.add_argument("data", help="Data to be encoded in the QR code.")
    parser.add_argument("filename", help="Output filename for the QR code image.")
    parser.add_argument("--style", choices=["classic", "dark", "colorful"], default="classic",
                        help="Style of the QR code. Choices are 'classic', 'dark', 'colorful'. Default is 'classic'.")

    args = parser.parse_args()
    print(args)

    if args.style == "classic":
        create_classic_qr_code(args.data, args.filename)
    elif args.style == "dark":
        create_dark_qr_code(args.data, args.filename)
    elif args.style == "colorful":
        create_colorful_qr_code(args.data, args.filename)
