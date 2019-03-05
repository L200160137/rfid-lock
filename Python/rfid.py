f = open('rfid.txt', 'r')
baris = f.readlines()
i = len(baris)
for j in range (0, i - 1):
    x = baris[j].split(' ')
    y = ','.join(x)
    z = y.rstrip()
    kurung = '{'+z+'},'
    print(kurung)
