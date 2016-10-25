__author__ = "Nickolas Howell"
import os

wordsUsed = {}
product = ""

keyDefault = """
{|} !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz"""

keyLibrary = {1: '{', 2: '|', 3: '}', 4: ' ', 5: '!', 6: '"', 7: '#', 8: '$', 9: '%', 10: '&', 11: "'", 12: '(', 13: ')', 14: '*', 15: '+', 16: ',', 17: '-', 18: '.',
              19: '/', 20: '0', 21: '1', 22: '2', 23: '3', 24: '4', 25: '5', 26: '6', 27: '7', 28: '8', 29: '9', 30: ':', 31: ';', 32: '<', 33: '=', 34: '>', 35: '?',
              36: '@', 37: 'A', 38: 'B', 39: 'C', 40: 'D', 41: 'E', 42: 'F', 43: 'G', 44: 'H', 45: 'I', 46: 'J', 47: 'K', 48: 'L', 49: 'M', 50: 'N', 51: 'O', 52: 'P',
              53: 'Q', 54: 'R', 55: 'S', 56: 'T', 57: 'U', 58: 'V', 59: 'W', 60: 'X', 61: 'Y', 62: 'Z', 63: '[', 64: '\\', 65: ']', 66: '^', 67: '_', 68: '`', 69: 'a',
              70: 'b', 71: 'c', 72: 'd', 73: 'e', 74: 'f', 75: 'g', 76: 'h', 77: 'i', 78: 'j', 79: 'k', 80: 'l', 81: 'm', 82: 'n', 83: 'o', 84: 'p', 85: 'q', 86: 'r',
              87: 's', 88: 't', 89: 'u', 90: 'v', 91: 'w', 92: 'x', 93: 'y', 94: 'z', 95: "\n"
}

keyLibraryTwo = {' ': 4, '$': 8, '(': 12, ',': 16, '0': 20, '4': 24, '8': 28, '<': 32, '@': 36, 'D': 40, 'H': 44, 'L': 48, 'P': 52, 'T': 56, 'X': 60, '\\': 64,
                 '`': 68, 'd': 72, 'h': 76, 'l': 80, 'p': 84, 't': 88, 'x': 92, '|': 2, '#': 7, "'": 11, '+': 15, '/': 19, '3': 23, '7': 27, ';': 31, '?': 35,
                 'C': 39, 'G': 43, 'K': 47, 'O': 51, 'S': 55, 'W': 59, '[': 63, '_': 67, 'c': 71, 'g': 75, 'k': 79, 'o': 83, 's': 87, 'w': 91, '{': 1, '"': 6,
                 '&': 10, '*': 14, '.': 18, '2': 22, '6': 26, ':': 30, '>': 34, 'B': 38, 'F': 42, 'J': 46, 'N': 50, 'R': 54, 'V': 58, 'Z': 62, '^': 66, 'b': 70,
                 'f': 74, 'j': 78, 'n': 82, 'r': 86, 'v': 90, 'z': 94, '!': 5, '%': 9, ')': 13, '-': 17, '1': 21, '5': 25, '9': 29, '=': 33, 'A': 37, 'E': 41,
                 'I': 45, 'M': 49, 'Q': 53, 'U': 57, 'Y': 61, ']': 65, 'a': 69, 'e': 73, 'i': 77, 'm': 81, 'q': 85, 'u': 89, 'y': 93, '}': 3, "\n" : 95}


def errorReport():
    reportMsg = ""
    for words, value in wordsUsed.iteritems():
        testPassed = 0
        if wordsUsed[words] == 0:
            reportMsg += "Failure! wordsUsed value set to 0 on key %s\n" % (words)
            testPassed += 1

    if testPassed == 0:
        reportMsg += "wordsUsed test passed!"
    else:
        reportMsg += "wordsUsed test failed with %s errors!" % (testPassed)

    return reportMsg

def encrypt(plain,key):
    product = ""
    print plain
    for letter in plain:
        print letter
        product += keyLibrary[key[letter]]
    return product

def decrypt(cipher,key):
    product = ""
    for letter in cipher:
        product += key[keyLibraryTwo[letter]]

    return product

def processKey(key):
    processedKey = {}
    number = 1
    for letter in key:
        processedKey[letter] = number
        number += 1
    return processedKey

def processKeyDecrypt(key):
    processedKey = {}
    number = 1
    for letter in key:
        processedKey[number] = letter
        number += 1
    return processedKey

def clearWords():
    for value in wordsUsed:
        wordsUsed[value] = 0

def main():
    while True:
        os.system("clear")
        UInput = raw_input(">  ")
        if UInput == "encrypt":
            print"""1. Import from Plain.txt file
2. Quick entry
"""
            UInput = raw_input(">  ")
            if UInput == "1":

                clearWords() #Getting ready to add characters to key

                try:
                    tempFile = open("plain.txt","rb")
                    plainText = tempFile.read()
                    tempFile.flush()
                    tempFile.close()
                except IOError:
                    tempFile = open("plain.txt","wb+")
                    plainText = tempFile.read()
                    tempFile.flush()
                    tempFile.close()

                preInputKey = raw_input("Key : ")
                inputKey = ""

                print "Pre Processed: %s" % preInputKey #Standalone Key

                for key in keyDefault:
                    if wordsUsed[key] == 0:
                        preInputKey += key
                        wordsUsed[key] = 1

                print "Post Processed: %s" % (preInputKey) #Key converted into cipher. Almost ready. (still has duplicate characters)

                clearWords() #Have to clear to identify duplicate characters

                for key in preInputKey:
                    if wordsUsed[key] == 0:
                        inputKey += key
                        wordsUsed[key] = 1

                print "Refined Cipher : %s" % (inputKey) #All dupes removed in cipher.

                key = processKey(inputKey) #Converts cipher into dictionary with numeric values in according order of cipher, 1-93.
                cipherText = encrypt(plainText,key) #Coverts all letters into corresponding cipher letters according to order.

                os.system("clear")
                print cipherText
                justInputKey = inputKey.split("\n")[0]
                print "\nRefined Password: %s" %(justInputKey)

                quickWrite = open("output.txt","wb")
                quickWrite.write(cipherText)
                quickWrite.close()

            elif UInput == "2":

                clearWords() #Getting ready to add characters to key
                plainText = raw_input("Plain Text: ")
                preInputKey = raw_input("Key : ")
                inputKey = ""

                plainTextFile = open("plain.txt","w+")
                plainTextFile.write(plainText)
                plainTextFile.flush()
                plainTextFile.close()

                print "Pre Processed: %s" % preInputKey #Standalone Key

                for key in keyDefault:
                    if wordsUsed[key] == 0:
                        preInputKey += key
                        wordsUsed[key] = 1

                print "Post Processed: %s" % (preInputKey) #Key converted into cipher. Almost ready. (still has duplicate characters)

                clearWords() #Have to clear to identify duplicate characters

                for key in preInputKey:
                    if wordsUsed[key] == 0:
                        inputKey += key
                        wordsUsed[key] = 1

                print "Refined Cipher : %s" % (inputKey) #All dupes removed in cipher.

                key = processKey(inputKey) #Converts cipher into dictionary with numeric values in according order of cipher, 1-93.
                cipherText = encrypt(plainText,key) #Coverts all letters into corresponding cipher letters according to order.

                os.system("clear")
                print cipherText
                justInputKey = inputKey.split("\n")[0]
                print "\nRefined Password: %s" %(justInputKey)

                quickWrite = open("output.txt","wb")
                quickWrite.write(cipherText)
                quickWrite.close()

            else:

                print"Command not recognized, type 1 or 2."

            raw_input("...")
        elif UInput == "decrypt":
            clearWords()

            try:
                tempFile = open("cipher.txt","rb")
                cipherText = tempFile.read()
                tempFile.flush()
                tempFile.close()
            except IOError:
                tempFile = open("cipher.txt","wb+")
                cipherText = tempFile.read()
                tempFile.flush()
                tempFile.close()

            preInputKey = raw_input("Key : ")
            inputKey = ""

            print "Pre Processed: %s" % preInputKey #Standalone Key

            for key in keyDefault:
                if wordsUsed[key] == 0:
                    preInputKey += key
                    wordsUsed[key] = 1

            print "Post Processed: %s" % (preInputKey) #Key converted into cipher. Almost ready. (still has duplicate characters)

            clearWords() #Have to clear to identify duplicate characters

            for key in preInputKey:
                if wordsUsed[key] == 0:
                    inputKey += key
                    wordsUsed[key] = 1

            print "Refined Cipher : %s" % (inputKey) #All dupes removed in cipher.
            
            key = processKeyDecrypt(inputKey) #Takes newly created cipher and reverses text
            plainText = decrypt(cipherText,key) #Converts all cipher letters to plain text through algorithm.

            os.system("clear")
            print plainText
            quickWrite = open("output.txt","wb")
            quickWrite.write(plainText)
            quickWrite.flush()
            quickWrite.close()

            raw_input("...")
        else:
            print("Commmand not recognized")
            raw_input("...")
