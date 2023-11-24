#只处理大写，小写的话一行好长
def vigenere(en_or_de,text,keyword):
    result=""
    for i in range(len(text)):
        if en_or_de==0:
            result+=chr((ord(text[i]) - ord('A') + ord(keyword[i%len(keyword)]) - ord('A')) % 26 + ord('A'))
        else:
            result+=chr((ord(text[i]) - ord('A') - ord(keyword[i%len(keyword)]) + ord('A')) % 26 + ord('A'))
    return result