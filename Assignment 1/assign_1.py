import matplotlib.pyplot as plt
import time
import string
file= open ("pg1497.txt", encoding="utf8")
text = file.read().replace("\n", " " )
text = text.lower()

alphabet= (string.ascii_lowercase)
total = 0

a={}
b={}
for x in (alphabet):
    a[x]=text.count(x)
    total= total+text.count(x)
    

print(a)
print(len(a))
b=a.copy()
#print(b)
for x in (alphabet):
    b[x]=b[x]/total

print(b)

for x, b[x] in b.items():
    print('{}: {:.3f}%'.format(x, b[x] * 100.))

plt.bar(b.keys(), b.values(), color= 'red')
#plt.hist(b.values(), len(b.keys()), color= 'yellow')
plt.show()
print(time.process_time())