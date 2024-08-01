# Steganography and Image Comparison Project

This project provides tools for steganography in images and image comparison using perceptual hashing. It includes three main components: a text encoder for images, a text decoder for images, and an image comparator.

## Components

### 1. Image Text Encoder

The encoder allows for embedding hidden text into PNG images. The text is encoded into bits and inserted into the color channels (R, G, B) of the image. The code uses a specified number of bits (N) for each channel and fills the remaining space with null bits.

**Main Functions:**
- `text_to_bits(text)`: Converts text into a string of bits.
- `insert_text_into_image(image_path, text, n_bits)`: Embeds the text into the specified image.

### 2. Image Text Decoder

The decoder extracts hidden text from an image that has been modified by the encoder. The text is retrieved from the color channels of the image and converted back into a text string. The code detects an end marker to identify the end of the message and removes padding.

**Main Functions:**
- `bits_to_text(bits)`: Converts a string of bits back into text.
- `text_to_bits(text)`: Converts text into a string of bits.
- `extract_text_from_image(image_path, n_bits)`: Extracts the text from the specified image.

### 3. Image Comparator

The comparator checks for differences between two images using perceptual hashing. It calculates the perceptual hash for each image and determines the Hamming distance between the hashes to assess similarity.

**Main Functions:**
- `calculate_image_hash(image_path)`: Computes the perceptual hash of an image.
- `compare_images(image_path1, image_path2)`: Compares two images and calculates the Hamming distance between their hashes.

### 4. Image Difference

The first image is the original (left side), and the second is after embedding the encrypted text into the image.

- Image 1 Hash: `cccc0bcf3199cb32`
- Image 2 Hash: `cccc09cf3399cb32`

The Hamming distance between the image hashes is: `2`

![Downhill Street with a train in the middle ](https://iili.io/dA7y0s1.png)

## Installation

To use this project, you need to install the following Python libraries:

```bash
pip install pillow imagehash


