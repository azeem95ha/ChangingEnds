str1 = ['end','if', 'in', 'form', 'depending']
str2 = 'end'
def changIng (text):
    word = []
    if type(text)==list :
        for i in text :
            if len (i) < 3:
                word.append(i)
            elif i.endswith('ing'):
                i = i + 'ly'
                word.append(i)
            else:
                i = i +'ing'
                word.append(i)
        print (', '.join(word))
    else:
        if len(text)<3:
            print (text)
        elif text.endswith('ing'):
            text = text + 'ly'
        else:
            text = text + 'ing'
        print (text) 
    
print (changIng(str2))