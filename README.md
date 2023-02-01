<h1 align="center">Image Compression Using Huffman Coding</h1>

# Abstract

Compression is used about everywhere. Images are essential documents nowadays; to work with them in some applications, they need to be compressed, more or less, depending on the purpose of the application. The need for an efficient technique for the compression of Images is increasing because the raw images need large amounts of disk space, which is a significant disadvantage during transmission & storage. Various algorithms perform this compression differently; some are lossless and keep the same information as the original image, and others lose information when compressing the image. In this Project, we proposed the Lossless method of image compression and decompression using a simple coding technique called Huffman coding. This technique is simple in implementation and utilizes less memory.

# Introduction

Compression refers to reducing the quantity of data used to represent a file, image, or video content without excessively reducing the quality of the original data. Image compression is the application of data compression on digital images. In effect, the objective is to reduce the redundancy of the image data in order to be able to store or transmit data in an efficient form [1]. Data compression has become a requirement for most applications in different areas such as computer science, Information technology, communications, medicine, etc. In computer science, Data compression is defined as the science or the art of representing information in a compact form. It also reduces the number of bits required to store and/or transmit digital media. Compressing something means that you have a piece of data and decrease its size. There are different techniques, and they all have their advantages and disadvantages. Huffman coding is a lossless data compression technique. Huffman coding is based on the frequency of occurrence of a data item, i.e., a pixel in images. The technique uses fewer bits to encode the data into binary codes that occur more frequently. It is used in JPEG files.

# Fundamental for Compression

Compression can be divided into two categories:

-   Lossy Compression

    Lossy compression means that some data is lost when it is decompressed. Lossy compression is based on the assumption that the current data files save more information than human beings can "perceive". Thus, the irrelevant data can be removed.

-   Lossless Compression

    Lossless compression means that when the data is decompressed, the result is a bit-for-bit perfect match with the original one. The name lossless means "no data is lost"; the data is only saved more efficiently in its compressed state, but nothing is removed.

# Compression Principle
A common characteristic of most images is that the neighboring pixels are correlated and contain redundant information. The foremost task is to find a less correlated representation of the image. Two fundamental components of compression are:

1. Redundancy reduction: aims at removing duplication forms of the signal (Image/Text). 

2. Irrelevancy reduction: omits parts of the signal that will not be noticed by the signal receiver, namely the Human visual system. 

In an image, there are three types of redundancies to compress file size. They are: 

1. Coding redundancy: Fewer bits to represent frequently occurring symbols. 

2. Interpixel redundancy: Neighboring pixels have almost the same value. 

3. Psyco visual redundancy: Human visual system cannot simultaneously distinguish all colors. 
# Huffman Coding 
Huffman coding is a classical data compression technique invented by David Huffman. It is optimal prefix code generated from a set of probabilities and has been used in various compression applications. These codes are of variable code length using the integral number of bits. This idea causes a reduction in the average code length, and thus overall size of compressed data is smaller than the original. 

Huffman code procedure is based on two observations:
1. More frequently occurred symbols will have shorter code words than a symbol that occurs less frequently. 
2. The two symbols that occur least frequently will have the same length. 

The Huffman code is designed by merging the lowest probable symbols. This process is repeated until only two probabilities of two compound symbols are left; thus, a code tree is generated, and Huffman codes are obtained from labeling the code tree.

# Compression Ratio (CR) 
Compression ratio (CR) is defined as the number of bits representing the original image's size to the number of bits representing the compressed image's size. The compression ratio shows how much time the image has been compressed. 

# Development of Huffman Compression & Decompressoin on an Image:
1. Read the image in binary mode as a string of bits
2. Calculate the frequency of each byte in the string of bits
3. Push each byte into a Min-Heap according to its frequency
4. Built Huffman-Tree by merging two lowest-frequent bytes from the Min-Heap and pushing them back while assigning binary directions
5. Save Huffman-Codes in a .txt file from the merged Huffman-Tree
6. Save the compressed string of bits from the Huffman-Codes in a .bin file
7. Calculate the compression ratio (CR) 
8. Decompress the compressed string of bits by reverse-mapping each byte from the calculated Huffman-Codes
