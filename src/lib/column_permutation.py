def column_permutation(en_or_de,text,keyword):
    text= ''.join(text.split())
    keyword= ''.join(keyword.split())
    keyword=keyword[:-len(keyword)+len(text)]if len(keyword)>len(text) else keyword
    keyword=list(keyword)
    sortkey=''.join(sorted(keyword))
    sortkey=list(sortkey)
    num=[]
    for i in range(len(sortkey)):
        num.append([(sortkey.index(keyword[i]))])
        if sortkey.count(keyword[i])>1:
            sortkey[sortkey.index(keyword[i])]=None
    if en_or_de==0:
        for i in range(len(text)):
            num[i%len(num)].append(text[i])
        num.sort(key=lambda x: x[0])
        result=''.join([''.join(item[1:])for item in num])
        return result
    else:
        for i in range(len(keyword)):
            if i<len(text)%len(keyword):
                num[i].append(len(text)//len(keyword)+1)
            else:
                num[i].append(len(text)//len(keyword))
        remain=0
        for i in range(len(keyword)):
            c=0
            for j in range(len(keyword)):
                if num[j][0]==i:
                    c=j
            for j in range(num[c][1]):
                num[c].append(text[remain+j])
            remain+=j+1
        result=''
        for i in range(len(num[1])-2):
            for j in range(len(keyword)):
                if(len(num[j])>2+i):
                    result+=num[j][2+i]
        return result