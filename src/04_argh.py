import argh
from argh import arg
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

@arg('data', help="Data to be encoded in the QR code.")
@arg('filename', help="Output filename for the QR code image.")
@arg('--style', choices=["classic", "dark", "colorful"], default="classic",
     help="Style of the QR code. Choices are 'classic', 'dark', 'colorful'. Default is 'classic'.")
def create_qr_code_cli(data, filename, style='classic'):
    if style == "classic":
        create_classic_qr_code(data, filename)
    elif style == "dark":
        create_dark_qr_code(data, filename)
    elif style == "colorful":
        create_colorful_qr_code(data, filename)

def main():
    # Argh dispatches commands
    argh.dispatch_command(create_qr_code_cli)

if __name__ == "__main__":
    main()
