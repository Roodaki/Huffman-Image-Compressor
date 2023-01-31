# A Function That Reads an Image as Binary Data and Returns a String of bits
def read_image_bit_string(path):
    with open(path, 'rb') as image:
        bit_string = ""
        byte = image.read(1)
        while (len(byte) > 0):
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = image.read(1)
    return bit_string


def write_image(bit_string, path):
    with open(path, 'wb') as image:
        for i in range(0, len(bit_string), 8):
            byte = bit_string[i:i + 8]
            image.write(bytes([int(byte, 2)]))


def write_dictionary_file(dictionary, path):
    with open(path, 'w') as f:
        for key, value in dictionary.items():
            f.write('%s:%s\n' % (key, value))