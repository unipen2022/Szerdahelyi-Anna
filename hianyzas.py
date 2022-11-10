def hetnapja(honap,nap):
    napnev =  {'vasarnap', 'hetfo', 'kedd', 'szerda', 'csutortok', 'pentek', 'szombat'} ;
    napszam = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335 }
    napsorszam = (napszam[honap-1]+nap) %  7
    hetnapja = napnev[napsorszam]
    return hetnapja

def igazolt(text):
   n = len(text)
   db = 0
   for i in range(0,n-1):
      temp = text[i:i+1]
      if temp == 'X':
         db = db + 1
   return db 

def igazolatlan(text):
   n = len(text)
   db = 0
   for i in range(0,n-1):
      temp = text[i:i+1]
      if temp == 'I':
         db = db + 1
   return db 


f = open('hianyzasok.txt','r')
for i in f:
   sor = i.strip()

