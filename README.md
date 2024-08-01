# Projeto de Esteganografia e Comparação de Imagens

Este projeto oferece ferramentas para esteganografia em imagens e comparação de imagens usando hash perceptual. O projeto inclui três componentes principais: um encoder de texto para imagens, um decoder de texto de imagens e um comparador de imagens.

## Componentes

### 1. Encoder de Texto em Imagem

O encoder permite a inserção de texto oculto em imagens PNG. O texto é codificado em bits e inserido nos canais de cor (R, G, B) da imagem. O código utiliza um número definido de bits (N) para cada canal e preenche os espaços restantes com bits nulos.

**Funções principais:**
- `text_to_bits(text)`: Converte o texto em uma string de bits.
- `insert_text_into_image(image_path, text, n_bits)`: Insere o texto na imagem especificada.

### 2. Decoder de Texto em Imagem

O decoder extrai texto oculto de uma imagem que foi modificada pelo encoder. O texto é recuperado dos canais de cor da imagem e convertido de volta em uma string de texto. O código detecta um marcador de fim para identificar o final da mensagem e remove o padding.

**Funções principais:**
- `bits_to_text(bits)`: Converte uma string de bits de volta em texto.
- `text_to_bits(text)`: Converte texto em uma string de bits.
- `extract_text_from_image(image_path, n_bits)`: Extrai o texto da imagem especificada.

### 3. Comparador de Imagens

O comparador verifica as diferenças entre duas imagens usando hash perceptual. Ele calcula o hash perceptual para cada imagem e determina a distância Hamming entre os hashes para avaliar a similaridade.

**Funções principais:**
- `calculate_image_hash(image_path)`: Calcula o hash perceptual de uma imagem.
- `compare_images(image_path1, image_path2)`: Compara duas imagens e calcula a distância Hamming entre seus hashes.

## Instalação

Para usar este projeto, você precisa instalar as seguintes bibliotecas Python:

```bash
pip install pillow imagehash
