#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode(): #defines function
    while True:
        print('Do you wish to encrypt or decrypt a message?') #asks for a choice between encrypt or de
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #if you give input of encrypt, or decrypt, then you can move on
            return mode #returns this function back into the program
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') #if you give illegal word, then this comes up

def getMessage(): #define function
    print('Enter your message: ') #enters message
    return input() #gives input to getMessage

def getKey(): #function
    key = 0 #sets key to equal 0
    while True: # onyl if its true
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) # print statement
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key #key minus key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key))
