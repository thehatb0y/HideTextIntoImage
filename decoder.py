from PIL import Image

def bits_to_text(bits):
    """Converte uma string de bits em texto."""
    text = ''
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte:
            text += chr(int(byte, 2))
    return text

def text_to_bits(text):
    """Converte o texto em uma string de bits."""
    return ''.join(format(ord(c), '08b') for c in text)

def extract_text_from_image(image_path, n_bits=3):
    """Extrai o texto de uma imagem PNG utilizando esteganografia LSB."""
    img = Image.open(image_path)
    # Certifica-se de que a imagem está em RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    pixels = img.load()
    width, height = img.size
    bits_per_pixel = 3 * n_bits

    text_bits = ''
    marker_bits = text_to_bits('--')
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Concatena os bits dos canais R, G e B
            text_bits += format(r & ((1 << n_bits) - 1), '0' + str(n_bits) + 'b')
            text_bits += format(g & ((1 << n_bits) - 1), '0' + str(n_bits) + 'b')
            text_bits += format(b & ((1 << n_bits) - 1), '0' + str(n_bits) + 'b')
            
            # Se encontrar o marcador de fim, pare a leitura
            if marker_bits in text_bits:
                text_bits = text_bits[:text_bits.index(marker_bits)]
                break
        else:
            continue
        break
    
    # Converte bits para texto e remove qualquer padding nulo
    text = bits_to_text(text_bits)
    return text.rstrip('\x00').rstrip()

# Exemplo de uso
extracted_text = extract_text_from_image('output_image.png', n_bits=3)
print(f"Texto extraído: {extracted_text}")
