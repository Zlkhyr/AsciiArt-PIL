from PIL import Image, ImageEnhance
import sys

ASCII = "@%#*+=-:. "
# ASCII = " .:-=+*#%@"

def resize_gambar(gambar, lebar_baru=100):
    lebar, tinggi = gambar.size
    rasio = tinggi / lebar
    tinggi_baru = int(lebar_baru * rasio * 0.55)
    return gambar.resize((lebar_baru, tinggi_baru))

def pixels_to_ascii(gambar):
    pixels = gambar.get_flattened_data()
    range = 255 // (len(ASCII)-1)
    ascii_str = ""
    for pixel in pixels:
        index = pixel // range
        if index >= len(ASCII):
            index = len(ASCII) - 1
        ascii_str += ASCII[index]
    return ascii_str

def gambar_ke_ascii(gambar, width=100):
    try:
        gambar = Image.open(gambar)
    except FileNotFoundError:
        return f"Gambar {gambar} tidak ditemukan!"

    gambar = resize_gambar(gambar, width)
    gambar = gambar.convert("L")
    gambar = ImageEnhance.Contrast(gambar).enhance(1.8)
    gambar = ImageEnhance.Sharpness(gambar).enhance(5)

    ascii_str = pixels_to_ascii(gambar)
    img_width = gambar.width

    ascii_img = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    return ascii_img

def main():
    if len(sys.argv) < 3:
        print("Penggunaan: python AsciiART.py <path_gambar> <lebar_ascii>")
        sys.exit(1)
    print(gambar_ke_ascii(sys.argv[1], int(sys.argv[2])))

if __name__ == "__main__":
    main()

