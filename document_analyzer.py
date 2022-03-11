'''
Inderpreet Singh
CMPE-131 Sec 02
HW2 - Q2
'''
def document_analyzer(filename):
    file = open(filename, 'r', encoding='utf8')
    print('\r')
    fl=file.read()
    words=fl.split();

    words.sort()

    freq={}
    
    for i in words:
        if(i in freq.keys()):
            freq[i] += 1
        else:
            freq[i] = 1
    top5 = sorted(freq, key = freq.get, reverse = True)[:5] #this is used to sort all the keys based on the values and then slice the top 5
    
    for i in top5:
        print(i+':',freq[i])    
    file.close()

document_analyzer("document.txt")
