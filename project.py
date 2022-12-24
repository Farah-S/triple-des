#variables
key1 = 'A6F42BD15C61F4C9';
key2 = 'FB36A2C73D2C90E5';
key3 = '2E4C65A2E836B73A';

s_box1 = [[1, 14, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 5, 7, 14, 4, 12, 13, 1, 10, 6, 2, 11, 9, 15, 3, 8],
         [4, 1, 14, 8, 3, 6, 2, 11, 15, 12, 9, 7, 13, 0, 5, 10],
         [15, 2, 8, 12, 4, 9, 1, 7, 5, 11, 13, 14, 0, 10, 6, 3]];

s_box2 = [[5, 11, 8, 14, 6, 1, 13, 4, 9, 7, 12, 3, 2, 10, 15, 0],
         [13, 3, 14, 7, 15, 12, 8, 4, 2, 0, 10, 11, 6, 9, 1, 5],
         [10, 4, 7, 1, 0, 14, 13, 11, 15, 8, 12, 9, 6, 3, 5, 2],
         [3, 8, 0, 11, 13, 15, 4, 12, 1, 6, 7, 2, 10, 5, 14, 9]];

s_box3 = [[0, 10, 9, 4, 6, 13, 15, 5, 11, 3, 2, 7, 1, 14, 12, 8],
         [3, 7, 1, 9, 13, 14, 6, 11, 12, 8, 5, 4, 2, 10, 15, 0],
         [10, 6, 14, 9, 8, 5, 3, 0, 11, 1, 12, 2, 15, 13, 4, 7],
         [11, 0, 3, 10, 6, 9, 8, 7, 14, 15, 4, 13, 1, 5, 12, 2]];

s_box4 = [[7, 3, 4, 13, 0, 6, 9, 1, 10, 12, 8, 5, 11, 2, 14, 15],
         [3, 8, 1, 15, 6, 5, 0, 13, 14, 7, 12, 2, 10, 11, 4, 9],
         [0, 6, 9, 10, 2, 1, 7, 3, 5, 11, 13, 14, 15, 12, 8, 4],
         [13, 5, 10, 6, 1, 0, 3, 8, 9, 4, 15, 11, 2, 7, 12, 14]];

s_box5 = [[12, 2, 14, 10, 7, 11, 1, 6, 8, 15, 13, 5, 3, 0, 4, 9],
         [4, 1, 12, 2, 14, 7, 3, 11, 15, 10, 5, 0, 13, 9, 8, 6],
         [14, 12, 10, 1, 11, 3, 7, 8, 5, 9, 2, 15, 6, 13, 0, 4],
         [1, 8, 2, 7, 11, 4, 12, 3, 6, 5, 10, 9, 0, 14, 15, 13]];

s_box6 = [[2, 10, 11, 5, 9, 12, 6, 8, 0, 3, 13, 14, 4, 7, 15, 1],
         [0, 5, 14, 12, 7, 2, 9, 15, 6, 11, 3, 4, 10, 1, 13, 8],
         [9, 4, 5, 15, 12, 8, 2, 13, 7, 10, 14, 0, 11, 3, 1, 6],
         [14, 13, 12, 2, 9, 15, 5, 0, 1, 4, 11, 7, 6, 10, 8, 3]];

s_box7 = [[14, 1, 12, 4, 5, 10, 8, 3, 13, 2, 9, 7, 15, 0, 6, 11],
         [3, 10, 1, 7, 14, 9, 11, 0, 4, 13, 15, 2, 12, 5, 8, 6],
         [11, 14, 1, 3, 2, 13, 7, 4, 0, 5, 6, 8, 10, 15, 9, 12],
         [6, 1, 3, 8, 11, 14, 0, 7, 9, 15, 10, 5, 4, 12, 13, 2]];

s_box8 = [[3, 12, 8, 14, 6, 5, 1, 11, 0, 9, 13, 4, 15, 10, 2, 7],
         [11, 5, 3, 8, 0, 13, 7, 14, 2, 15, 6, 1, 10, 4, 9, 12],
         [7, 1, 14, 11, 9, 2, 4, 12, 10, 6, 0, 3, 5, 13, 15, 8],
         [12, 11, 4, 7, 14, 0, 8, 3, 5, 2, 9, 10, 13, 15, 6, 1]];

initial_perm = [11,58,33,12,45,1,20,18,13,38, 6,29,9,22,64,60,21,8,36,41, 17,14,54,42,34,30,49,53,56,26, 61,44,50,62,52,47,27,10,39,28, 7,24,57,32,5,63,19,55,30,3, 59,35,40,23,48,4,43,2,51,16, 31,25,46,15];

expansion_perm = [32, 1, 2, 3, 4, 5, 6, 7, 6, 7, 8, 9, 10, 11, 10, 11, 12, 13, 14, 13, 14, 15, 16, 17, 18, 17, 18, 19, 20, 21, 22, 21, 22, 23, 24, 25, 26, 25, 26, 27, 28, 29, 30, 29, 30, 31, 32, 11];

straight_perm = [6, 17, 2, 12, 28, 21, 29, 7, 1, 5, 31, 26, 15, 18, 23, 11, 20, 8, 25, 4, 32, 30, 3, 19, 9, 13, 27, 16, 22, 10, 14, 24];

final_perm = [4, 48, 8, 56, 16, 64, 24, 31, 63, 47, 7, 55, 5, 32, 39, 23, 30, 46, 6, 54, 14, 62, 22, 38, 13, 53, 29, 37, 5, 21, 61, 45, 28, 44, 40, 20, 60, 12, 52, 36, 3, 35, 43, 11, 59, 27, 51, 19, 42, 2, 34, 50, 10, 58, 18, 26, 33, 41, 1, 49, 9, 57, 17, 25];

key_parity = [17, 41, 49, 34, 25, 57, 9,
                18, 50, 58, 26, 33, 42, 1,
                51, 27, 59, 10, 35, 3, 2,
                11, 19, 36, 44, 52, 60, 43,
                23, 5, 47, 31, 39, 63, 55,
                7, 46, 38, 62, 54, 22, 30,
                45, 61, 6, 37, 14, 53, 29,
                12, 4, 15, 20, 28, 21, 13];
    
left_shift_per_Round = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1];
    
key_compression = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32];

#---------------------------------------------------------------------    

#key generation for the 16 rounds
def generateKeys(key):
    roundKeys=[];
    binKey=stringToBinray(key);
    
    #perform parity drop
    key56bit = dropKeyParity(binKey);
    
    #split key
    leftKey=key56bit[:28];
    rightKey=key56bit[28:];
    
    #get round keys
    for i in range(16):
        #left shift depending on round number
        shiftedLeft=leftShift(leftKey,left_shift_per_Round[i]);
        shiftedRight=leftShift(rightKey,left_shift_per_Round[i]);
        #combine keys again
        combinedKey=shiftedLeft+shiftedRight;
        #use compression table to get 48 bit key from 56 bits
        compressedKey=compressKey(combinedKey);
        #add key of the i-th round
        roundKeys.append(compressedKey);
        
        leftKey=shiftedLeft;
        rightKey=shiftedRight;
    return roundKeys;


def dropKeyParity(key):
    newKey = ''
    for i in range(len(key_parity)):
        index = key_parity[i] - 1
        newKey = newKey + key[index];
    return newKey;


def leftShift(key,shiftAmount):
    newKey = key[shiftAmount:];
    for i in range(shiftAmount):
        newKey = newKey + key[i];
    return newKey;


def compressKey(key):
    roundKey = '';
    for i in range(len(key_compression)):
        index = key_compression[i] - 1;
        roundKey = roundKey + key[index];
    # print(len(roundKey));
    return roundKey;

#---------------------------------------------------------------------    

#initial permutation
def initialPermutation(plain):
    return '';


#expansion permutation
def expansionPermutation(plain):
    return '';


#XOR with key
def XOR(plain, key):
    return '';


#S-Box
def SBox(plain, s_box):
    return '';


#straight permutation
def straightPermutation(plain):
    return '';


#swap
def swap(plain):
    return '';


#final permutation
def finalPermutation(plain):
    return '';

#---------------------------------------------------------------------    

#takes input string and transforms it into binary
def stringToBinray(string):
    return ''.join(format(i, '08b') for i in bytearray(string, encoding ='utf-8'));


#takes binary and transforms it into string
def binaryToString(binary):
    #convert binary to int
    intString = int(binary, 2);
    #convert int to hexadecimal
    hexaString = format(intString, 'x');
    return(hexaString);


#splits the string into 64 bit blocks
def divideToBlocks(bin):
    length = len(bin);
    if length % 64 != 0:
        for j in range(64-length%64):
            bin = bin+'0';
        length = len(bin);
    blocks = []
    for i in range(0, length, 64):
        # print(bin[i:i+64]);
        blocks.append(bin[i:i+64]);
    # print(blocks)
    return blocks;

#---------------------------------------------------------------------    

#encyrption and decryption of normal DES
def DESencrypt(key, block):
    roundKeys = generateKeys(key);
    print(roundKeys);
    return '';
    
    
def DESdecrypt(key, block):
    roundKeys = generateKeys(key);
    print(roundKeys);
    return '';
    
#---------------------------------------------------------------------    
    
#encyrption and decryption of triple DES
def tripleDESencrypt(plainBlocks):
    cipherBinary = '';
    for i in range(len(plainBlocks)):
        enc1 = DESencrypt(key1,plainBlocks[i]);
        dec = DESdecrypt(key2,enc1);
        enc2 = DESencrypt(key3,dec);
        cipherBinary = cipherBinary + enc2;
    return cipherBinary;


def tripleDESdecrypt(cipherBlocks):
    plainBinary = '';
    for i in range(len(cipherBlocks)):
        dec1 = DESdecrypt(key3,cipherBlocks[i]);
        enc = DESencrypt(key2,dec1);
        dec2 = DESdecrypt(key1,enc);
        plainBinary = plainBinary + dec2;
    return plainBinary;

#---------------------------------------------------------------------    

inputString = input('Enter plain text:');
binary = stringToBinray(inputString);
#encrypt
plainBlocks = divideToBlocks(binary);
cipherBinary = tripleDESencrypt(plainBlocks);
cipherText = binaryToString(cipherBinary);
#decrypt
cipherBlocks = divideToBlocks(binary);
plainBinary = tripleDESdecrypt(cipherBlocks);
plainText = binaryToString(plainBinary);
