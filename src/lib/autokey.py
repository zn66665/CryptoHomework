#只处理大写
def autokey(en_or_de,text,keyword):
    text= ''.join(text.split())
    keyword= ''.join(keyword.split())
    result=""
    if en_or_de==0:
        a=len(keyword)
        keyword=keyword+text
        keyword=keyword[:-a]
        for i in range(len(text)):
            result+=chr((ord(text[i]) - ord('A') + ord(keyword[i%len(keyword)]) - ord('A')) % 26 + ord('A'))
    else:
        for i in range(len(text)):
            result+=chr((ord(text[i]) - ord('A') - ord(keyword[i]) + ord('A')) % 26 + ord('A'))
            if i==len(keyword)-1:
                keyword+=chr((ord(text[i]) - ord('A') - ord(keyword[i]) + ord('A')) % 26 + ord('A'))
    return result