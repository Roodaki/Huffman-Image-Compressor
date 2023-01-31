import file_handling
import huffman_coding

image_path = input("Image Path: ")  # IO/Inputs/Cat.jpg
image_bit_string = file_handling.read_image_bit_string(image_path)
compressed_image_bit_string = huffman_coding.compress(image_bit_string)
file_handling.write_image(compressed_image_bit_string,
                          "IO/Outputs/compressed_image.jpg")
print("Compression Ratio (CR):",
      len(image_bit_string) / len(compressed_image_bit_string))
decompressed_image_bit_string = huffman_coding.decompress(
    compressed_image_bit_string)
file_handling.write_image(decompressed_image_bit_string,
                          "IO/Outputs/decompressed_image.jpg")