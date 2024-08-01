from PIL import Image
import fitz

def text_to_bits(text):
    """Converte o texto em uma string de bits."""
    return ''.join(format(ord(c), '08b') for c in text)

def insert_text_into_image(image_path, text, n_bits=3):
    """Insere texto em uma imagem PNG utilizando esteganografia LSB."""
    img = Image.open(image_path)
    # Certifica-se de que a imagem está em RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = img.load()
    width, height = img.size
    total_pixels = width * height
    bits_per_pixel = 3 * n_bits  # 3 canais (R, G, B) * N bits por canal
    
    # Calcula quantos caracteres podem ser inseridos
    bits_available = total_pixels * bits_per_pixel
    text_bits = text_to_bits(text) + text_to_bits('--')  # Adiciona bits do marcador de fim
    bits_needed = len(text_bits)
    
    if bits_needed > bits_available:
        raise ValueError("Texto muito longo para ser inserido na imagem.")
    
    text_bits = text_bits.ljust(bits_available, '0')  # Preencher com 0s
    bit_index = 0
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Extraímos e ajustamos os N bits de cada canal
            new_r = (r & ~((1 << n_bits) - 1)) | int(text_bits[bit_index:bit_index + n_bits], 2)
            bit_index += n_bits
            
            new_g = (g & ~((1 << n_bits) - 1)) | int(text_bits[bit_index:bit_index + n_bits], 2)
            bit_index += n_bits
            
            new_b = (b & ~((1 << n_bits) - 1)) | int(text_bits[bit_index:bit_index + n_bits], 2)
            bit_index += n_bits
            
            pixels[x, y] = (new_r, new_g, new_b)
            
            # Verifica se a inserção do texto está completa
            if bit_index >= len(text_bits):
                img.save("output_image.png")
                print(f"Imagem processada e salva como output_image.png")
                print(f"Total de pixels: {total_pixels}")
                print(f"Caracteres que podem ser inseridos: {bits_available // 8}")
                return

    # Salva a imagem se o loop terminar
    img.save("output_image.png")
    print(f"Imagem processada e salva como output_image.png")
    print(f"Total de pixels: {total_pixels}")
    print(f"Caracteres que podem ser inseridos: {bits_available // 8}")

def extract_text_from_pdf(pdf_path):
    """Extrai texto de um PDF."""
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

# Exemplo de uso
text = "Insert your text here."
insert_text_into_image('input_image.png', text, n_bits=3)
