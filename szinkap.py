f = open('kep.txt','r')
n = 50 * 50
pont = {}
X = []
Y = []
db = 0
for i in f:
    sor = i.strip().split(' ')
    pont['R'] = int(sor[0])
    pont['G'] = int(sor[1])
    pont['B'] = int(sor[2])
    X.append(pont)
    pont = {}
""""
R = input('R:')
G = input('G:')
B = input('B:')
van = False
for i in range(0,n):
    temp = X[i]
    if temp['R'] == R and temp['G'] == G and temp['B'] ==B:
        van = True
if van == True:
    print('Van ilyen kód!')
else:
    print('Nincs ilyen kód!')
"""
index = 33 * 50 + 8
temp = X[index]
tol = 34 * 50
ig  = tol + 50
db = 0
for i in range(tol,ig):
    if X[i] == temp:
        db = db + 1
print('Ez a szin {0} alkalommal szerepel'.format(db))
p = 0
k = 0
z = 0
for i in range(0,n):
    temp = X[i]
    if temp['R'] == 255 and temp['G'] == 0 and temp['B'] == 0:
        p = p + 1
    elif temp['R'] == 0 and temp['G'] == 255 and temp['B'] == 0:
        z = z + 1
    elif temp['R'] == 0 and temp['G'] == 0 and temp['B'] == 255:
        k = k + 1
print(p,z,k)
if p > k and p > z:
    print('Piros volt többször')
elif k > p and k > z:
    print('Kék volt többször')
else:
    print('Zöld volt többször')

out = open('keretes.txt','w')
for i in range(0,n):
    temp = X[i]
    txt = str(temp['R']) +' '+ str(temp['G'])+' '+str(temp['B']) 
    out.write(txt+'\n')
out.close()

i = 0
temp = X[i]
while i < n and not(temp['R'] == 255 and temp['G'] == 255 and temp['B'] == 0):
    i = i + 1
    temp = X[i]
sor_1 = i // 50
oszlop_1 = i % 50
print('Sor:',sor_1,'Oszlop:',oszlop_1)

i = n-1
temp = X[i]
while i < n and not(temp['R'] == 255 and temp['G'] == 255 and temp['B'] == 0):
    i = i - 1
    temp = X[i]
sor_1 = i // 50
oszlop_1 = i % 50
print('Sor:',sor_1,'Oszlop:',oszlop_1)