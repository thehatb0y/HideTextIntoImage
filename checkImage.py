from PIL import Image
import imagehash

def calculate_image_hash(image_path):
    """Calcula o hash perceptual de uma imagem."""
    image = Image.open(image_path)
    return imagehash.phash(image)  # Usando o hash perceptual (phash)

def compare_images(image_path1, image_path2):
    """Compara duas imagens usando hash perceptual e calcula a distância entre eles."""
    hash1 = calculate_image_hash(image_path1)
    hash2 = calculate_image_hash(image_path2)

    print(f"Hash da imagem 1: {hash1}")
    print(f"Hash da imagem 2: {hash2}")
    
    # Calcula a distância Hamming entre os hashes
    hamming_distance = hash1 - hash2

    return hamming_distance

# Caminhos para as imagens a serem comparadas
image1_path = 'input_image.png'
image2_path = 'output_image.png'

# Comparar as imagens
difference = compare_images(image1_path, image2_path)

print(f"A distância entre os hashes das imagens é: {difference}")

if difference == 0:
    print("As imagens são idênticas.")
else:
    print("As imagens são diferentes.")
