import random as ra

def lue(filu):
    with open(filu, 'r') as f:
        redata = f.read()
    cledata = ''.join(e for e in redata if e.isalpha() or e.isspace())
    cledata = cledata.lower()
    cledata = ' '.join(cledata.split())
    cledata = cledata.strip()
    return cledata

def crunch(daata):    
    radata = daata
    lerray = list(set(radata))
    sta=len(lerray)
    prorray=[[0]*sta for _ in range(sta)]
    for k in range(len(radata)-1):
        prorray[lerray.index(radata[k])][lerray.index(radata[k+1])] += 1
    for row in prorray:
        n=sum(row)
        if n > 0:
            row[:] = [f/sum(row) for f in row]
    rerray = [lerray, prorray]
    return rerray
    
def words(many, marko):
    lerray = marko[0]
    prorray = marko[1]
    sana=''
    lista=[]
    kirj =''
    while len(lista) < many:
        kirj=ra.choice(lerray)
        while not kirj ==' ':
            sana += kirj
            prob = ra.random()
            j=0
            k=0
            for i in prorray[lerray.index(kirj)]:
                j += i
                
                if j > prob:
                    kirj = lerray[k]
                    break
                k +=1
        if len(sana)>=4:
            lista.append(sana)
        sana=''
    for i in lista:
        print(i)
                
            
        
    
    

words(100, crunch(lue('pg2000.txt')))

    
    