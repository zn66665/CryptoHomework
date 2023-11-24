#处理大小写
def caesar(en_or_de,text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                if en_or_de==0:
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                if en_or_de==0:
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                else:
                    result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result
print(caesar(1,'saandsa',2))