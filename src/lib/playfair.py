def playfair(en_or_de,text,keyword):
    result=""
    text= ''.join(text.split())
    keyword= ''.join(keyword.split())
    text=text.upper()
    keyword=keyword.upper()
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword= ''.join(sorted(set(keyword), key=keyword.index))
    alphabet=keyword+alphabet
    alphabet= ''.join(sorted(set(alphabet), key=alphabet.index))
    if en_or_de==0:
        i=0
        while i<len(text)-1:
            if text[i]==text[i+1]:
                text=text[:i+1] +"X"+text[i+1:]
                i+=2
            else:
                i+=1
        if len(text)%2==1:
            text+='X'
        text=text.replace("J", "I")
        for i in range(0,len(text)-1,2):
            p=alphabet.index(text[i])
            q=alphabet.index(text[i+1])
            if p//5==q//5:
                if (p+1)%5==0:
                    result+=alphabet[p-4]
                else:
                    result+=alphabet[p+1]
                if (q+1)%5==0:
                    result+=alphabet[q-4]
                else:
                    result+=alphabet[q+1]
            elif (q-p)%5==0:
                if p+5>24:
                    result+=alphabet[p-20]
                else:
                    result+=alphabet[p+5]
                if q+5>24:
                    result+=alphabet[q-20]
                else:
                    result+=alphabet[q+5]
            else:
                result+=alphabet[p//5*5+q%5]
                result+=alphabet[q//5*5+p%5]
    else:
        for i in range(0,len(text)-1,2):
            p=alphabet.index(text[i])
            q=alphabet.index(text[i+1])
            if p//5==q//5:
                if p%5==0:
                    result+=alphabet[p+4]
                else:
                    result+=alphabet[p-1]
                if q%5==0:
                    result+=alphabet[q+4]
                else:
                    result+=alphabet[q-1]
            elif (q-p)%5==0:
                if p-5<0:
                    result+=alphabet[p+20]
                else:
                    result+=alphabet[p-5]
                if q-5<0:
                    result+=alphabet[q+20]
                else:
                    result+=alphabet[q-5]
            else:
                result+=alphabet[p//5*5+q%5]
                result+=alphabet[q//5*5+p%5]
    return result