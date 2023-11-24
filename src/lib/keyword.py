#只处理大写
def key(en_or_de,text, keyword):
    text= ''.join(text.split())
    keyword= ''.join(keyword.split())
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyword=keyword.upper()
    text=text.upper()
    keyword= ''.join(sorted(set(keyword), key=keyword.index))
    alphabet=keyword+alphabet
    alphabet= ''.join(sorted(set(alphabet), key=alphabet.index))
    result=""
    for c in text:
        if en_or_de==0:
            result+=alphabet[ord(c)-65]
        else:
            result += chr(alphabet.index(c) + 65)
    return result
