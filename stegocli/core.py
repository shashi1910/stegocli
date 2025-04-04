from PIL import Image

def encode_image(image_path, output_path, secret_text):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    idx = 0

    secret_text += '###'  # delimiter to indicate end of message
    binary_secret = ''.join(format(ord(i), '08b') for i in secret_text)

    for row in range(height):
        for col in range(width):
            if idx < len(binary_secret):
                r, g, b = img.getpixel((col, row))
                r = (r & ~1) | int(binary_secret[idx])  # store in LSB
                encoded.putpixel((col, row), (r, g, b))
                idx += 1
            else:
                break

    encoded.save(output_path)
    return True


def decode_image(image_path):
    img = Image.open(image_path)
    binary_data = ''
    width, height = img.size

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for c in chars:
        char = chr(int(c, 2))
        message += char
        if message.endswith('###'):
            break

    return message[:-3]  # remove delimiter
