# variables
key1 = 'A6F42BD15C61F4C9'
key2 = 'FB36A2C73D2C90E5'
key3 = '2E4C65A2E836B73A'

s_box1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

s_box2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

s_box3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

s_box4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

s_box5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

s_box6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

s_box7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s_box8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

s_boxes = [s_box1, s_box2, s_box3, s_box4, s_box5, s_box6, s_box7, s_box8]

initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
expansion_perm = [32, 1, 2, 3, 4, 5, 4, 5,
         6, 7, 8, 9, 8, 9, 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1]
straight_perm = [16,  7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2,  8, 24, 14,
       32, 27,  3,  9,
       19, 13, 30,  6,
       22, 11,  4, 25]
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]
key_parity = [17, 41, 49, 34, 25, 57, 9,
              18, 50, 58, 26, 33, 42, 1,
              51, 27, 59, 10, 35, 3, 2,
              11, 19, 36, 44, 52, 60, 43,
              23, 5, 47, 31, 39, 63, 55,
              7, 46, 38, 62, 54, 22, 30,
              45, 61, 6, 37, 14, 53, 29,
              12, 4, 15, 20, 28, 21, 13]

left_shift_per_Round = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

key_compression = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13,
                   2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# ---------------------------------------------------------------------

# key generation for the 16 rounds
def generateKeys(key):
    roundKeys = []
    binKey = stringToBinary(key)

    # perform parity drop
    key56bit = dropKeyParity(binKey)

    # split key
    leftKey = key56bit[:28]
    rightKey = key56bit[28:]

    # get round keys
    for i in range(16):
        # left shift depending on round number
        shiftedLeft = leftShift(leftKey, left_shift_per_Round[i])
        shiftedRight = leftShift(rightKey, left_shift_per_Round[i])
        # combine keys again
        combinedKey = shiftedLeft+shiftedRight
        # use compression table to get 48 bit key from 56 bits
        compressedKey = compressKey(combinedKey)
        # add key of the i-th round
        roundKeys.append(compressedKey)

        leftKey = shiftedLeft
        rightKey = shiftedRight
    return roundKeys


def dropKeyParity(key):
    newKey = ''
    for i in range(len(key_parity)):
        index = key_parity[i] - 1
        newKey = newKey + key[index]
    return newKey


def leftShift(key, shiftAmount):
    newKey = key[shiftAmount:]
    for i in range(shiftAmount):
        newKey = newKey + key[i]
    return newKey


def compressKey(key):
    roundKey = ''
    for i in range(len(key_compression)):
        index = key_compression[i] - 1
        roundKey = roundKey + key[index]
    # print(len(roundKey));
    return roundKey

# ---------------------------------------------------------------------

# initial permutation
def initialPermutation(plain):
    return ''


# expansion permutation
def expansionPermutation(text):
    return ''


# XOR with key
def XOR(value1, value2):
    a_lenght=len(value1)
    b_lenght=len(value2)
    c_original_lenght=max(a_lenght,b_lenght)

    c = int(value1,2) ^ int(value2,2)
    c='{0:b}'.format(c)
    c=str(c)
    while (len(c)<c_original_lenght):
        c="0"+c
    return c


# S-Box
def SBox(text):
    six_bit_array = []
    j = 0
    final_s_box_output = ''

    for i in range(0, 48, 6):
        six_bit_array.append(text[i:i+6])

    # 101100
    for i in six_bit_array:
        first_elemnt = i[0:1]
        last_elemnt = i[5:6]
        row_num = first_elemnt+last_elemnt
        # converting the binary string to decimal int
        row_num = int(row_num, 2)

        column_num = i[1:5]
        # converting the binary string to decimal int
        column_num = int(column_num, 2)

        current_s_box = s_boxes[j]
        row_and_column_intersection = current_s_box[row_num][column_num]
        row_and_column_intersection=bin(row_and_column_intersection).replace("0b", "")
        row_and_column_intersection=str(row_and_column_intersection)
        while(len(row_and_column_intersection)<4):
            row_and_column_intersection="0"+row_and_column_intersection
        # row_and_column_intersection=bin(row_and_column_intersection).replace("0b", "")
        
        final_s_box_output += row_and_column_intersection
        j += 1

    return final_s_box_output


# straight permutation
def straightPermutation(text):
    y=""
    for i in range(len(straight_perm)):
        y+=text[straight_perm[i]-1]
    return y


# swap
def swap(text):
    i = int(len(text)/2)
    return (text[i:] + text[:i])


# final permutation
def finalPermutation(text):
    y=""
    for i in range(len(final_perm)):
        y=y+text[(final_perm[i]-1)]
    return y

# ---------------------------------------------------------------------

# takes input string and transforms it into binary


def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])


def stringToBinary(string):
    return ''.join(format(i, '08b') for i in bytearray(string, encoding='utf-8'))


# splits the string into 64 bit blocks
def divideToBlocks(bin):
    length = len(bin)
    if length % 64 != 0:
        for j in range((64 - length) % 64):
            bin = '0'+bin 
        length = len(bin)
    blocks = []
    for i in range(0, length, 64):
        # print(bin[i:i+64]);
        blocks.append(bin[i:i+64])
    # print(blocks)
    return blocks

# ---------------------------------------------------------------------

# encyrption and decryption of normal DES


def DESencrypt(keys, block):
    afterIP = initialPermutation(block)
    left = afterIP[:int(len(afterIP)/2)]

    right = afterIP[int(len(afterIP)/2):]
    
    for i in range(16):
        # print(len(right))
        expanded = expansionPermutation(right)
        # print(len(expanded))
        XORed = XOR(expanded, keys[i])
        afterSBox = SBox(XORed)
        # print(afterSBox)
        perm = straightPermutation(afterSBox)
        leftXright = XOR(left, perm)
        # print('ddddddddddddddddddd')
        # print(len(right))
        # print(len(leftXright))
        left = right
        right = leftXright
       
        # print("round "+str(i+1)+": " +toString(left+right))
    afterRounds = left + right
    swapped = swap(afterRounds)
    cipher = finalPermutation(swapped)
    # print(keys);
    return cipher


def DESdecrypt(keys, block):
    roundsK = keys[::-1]
    return DESencrypt(roundsK, block)

# ---------------------------------------------------------------------

# encyrption and decryption of triple DES


def tripleDESencrypt(blocks):
    cipherBin = ''
    key1rounds = generateKeys(key1)
    key2rounds = generateKeys(key2)
    key3rounds = generateKeys(key3)

    for i in range(len(blocks)):
        print("encrypt")
        enc1 = DESencrypt(key1rounds, blocks[i])
        print("decrypt")
        dec = DESdecrypt(key2rounds, enc1)
        print("encrypt")
        enc2 = DESencrypt(key3rounds, dec)
        cipherBin = cipherBin + enc2
    return cipherBin


def tripleDESdecrypt(blocks):
    plainBin = ''
    key1rounds = generateKeys(key1)
    key2rounds = generateKeys(key2)
    key3rounds = generateKeys(key3)

    for i in range(len(blocks)):
        dec1 = DESdecrypt(key3rounds, blocks[i])
        enc = DESencrypt(key2rounds, dec1)
        dec2 = DESdecrypt(key1rounds, enc)
        plainBin = plainBin + dec2
    return plainBin

# ---------------------------------------------------------------------


# inputString = input('Enter plain text:')
# binary = stringToBinary(inputString)
# # encrypt
# plainBlocks = divideToBlocks(binary)
# cipherBinary = tripleDESencrypt(plainBlocks)
# cipherText = toString(cipherBinary)
# # decrypt
# cipherBlocks = divideToBlocks(binary)
# plainBinary = tripleDESdecrypt(cipherBlocks)
# plainText = toString(plainBinary)




inputString = input('Enter plain text:')
# print(originalbinary)
# encrypt
originalbinary = stringToBinary(inputString)
plainBlocks = divideToBlocks((originalbinary))
# print(plainBlocks)
cipherBinary = tripleDESencrypt(plainBlocks)
cipherText = toString(cipherBinary)
print(cipherText)

# decrypt
cipherBlocks = divideToBlocks(cipherBinary)
plainBinary = tripleDESdecrypt(cipherBlocks)
plainText = toString(plainBinary)
# print(plainBinary)
print( plainText)