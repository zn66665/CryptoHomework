def rc4(en_or_de,text,key):
    text=text.encode('utf-8')
    key=key.encode('utf-8')
    s=list(range(256))
    j=0
    for i in range(256):
        j=(j+s[i]+key[i%len(key)])%256
        s[i],s[j]=s[j],s[i]
    i=0
    j=0
    st=[]
    result=[]
    for _ in range(len(text)):
        i=(i+1)%256
        j=(j+s[i]) % 256
        s[i], s[j] = s[j], s[i]
        st.append(s[(s[i]+s[j])%256])
        result.append(text[_]^st[-1])
    if en_or_de==0:
        result=''.join([format(byte, '02x') for byte in result])
    else:
        result=bytes(result).decode('utf-8')
    return result
