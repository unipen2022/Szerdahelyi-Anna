f = open('fogadoora.txt','r')
adat = {}
X = []
for i in f:
   sor = i.strip()
   adatok = sor.split(' ')
   adat['nev'] = adatok[0] + ' ' + adatok[1]
   adat['ido'] = adatok[2]
   adat['rogzites'] = adatok[3]
   X.append(adat)
   adat = {}
nev = input('Kérek egy nevet:')
db = 0 
for i in range(0,len(X)):
   if X[i]['nev'] == nev:
      db = db + 1
print('{0} néven {1} időpontfoglalás van.'.format(nev,db))
ido = input(('Adjon meg egy érvényes időpontot (pl. 17:10):'))
Y = []
for i in range(0,len(X)):
   if X[i]['ido'] == ido:
      Y.append(X[i]['nev'])
Y.sort()
for i in range(0,len(Y)):
   print(Y[i])
min = X[0]['ido']
index = 0
for i in range(1,len(X)):
   if min > X[i]['ido']:
      min   = X[i]['ido']
      index = i
print('Tanár neve          :' +  X[index]['nev'])
print('Foglalt időpont     :' +  X[index]['ido'])
print('Foglalás ideje      :' +  X[index]['rogzites'])
