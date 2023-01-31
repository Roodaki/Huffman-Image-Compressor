import heapq

import file_handling


class node:

    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huffman_direction = ''

    def __lt__(self, nxt):
        return self.frequency < nxt.frequency


huffman_codes = {}


def get_compressed_image(image_bit_string):
    compressed_image_bit_string = ""
    for i in range(0, len(image_bit_string), 8):
        byte = image_bit_string[i:i + 8]
        compressed_image_bit_string += huffman_codes[byte]
    return compressed_image_bit_string


def calculate_huffman_codes(node, code=''):
    code += node.huffman_direction
    if (node.left):
        calculate_huffman_codes(node.left, code)
    if (node.right):
        calculate_huffman_codes(node.right, code)
    if (not node.left and not node.right):
        huffman_codes[node.symbol] = code
    return huffman_codes


def get_merged_huffman_tree(byte_to_frequency):
    huffman_tree = []
    for byte, frequency in byte_to_frequency.items():
        heapq.heappush(huffman_tree, node(frequency, byte))
    while len(huffman_tree) > 1:
        left = heapq.heappop(huffman_tree)
        right = heapq.heappop(huffman_tree)
        left.huffman_direction = "0"
        right.huffman_direction = "1"
        merged_node = node(left.frequency + right.frequency,
                           left.symbol + right.symbol, left, right)
        heapq.heappush(huffman_tree, merged_node)
    return huffman_tree[0]


def get_frequency(image_bit_string):
    byte_to_frequency = {}
    for i in range(0, len(image_bit_string), 8):
        byte = image_bit_string[i:i + 8]
        if byte not in byte_to_frequency:
            byte_to_frequency[byte] = 0
        byte_to_frequency[byte] += 1
    return byte_to_frequency


def compress(image_bit_string):
    byte_to_frequency = get_frequency(image_bit_string)
    merged_huffman_tree = get_merged_huffman_tree(byte_to_frequency)
    calculate_huffman_codes(merged_huffman_tree)
    file_handling.write_dictionary_file(huffman_codes,
                                        "./IO/Outputs/huffman_codes.txt")
    return get_compressed_image(image_bit_string)


def decompress(compressed_image_bit_string):
    decompressed_image_bit_string = ""
    current_code = ""
    for bit in compressed_image_bit_string:
        current_code += bit
        for byte, code in huffman_codes.items():
            if current_code == code:
                decompressed_image_bit_string += byte
                current_code = ""
    return decompressed_image_bit_string