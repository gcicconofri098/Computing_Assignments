import matplotlib.pyplot as plt
import time
import string

#open the file, eliminate the formattation and make all the letter lower case
file= open ("pg1497.txt", encoding="utf8") 
text = file.read().replace("\n", " " )
text = text.lower()

#call the alphabet letters, ordered
alphabet= (string.ascii_lowercase)
#define the total number of letters and create a dictionary
total = 0
a={}
#fill the dictionary and update the total number of letters
for x in (alphabet):
    a[x]=text.count(x)
    total= total+text.count(x)
    
#print check
print(a)
print(len(a))

#substitute the total number of a specific letter with the relative frequency
for x in (alphabet):
    a[x]=a[x]/total

#print the relative frequencies
for x, a[x] in a.items():
    print('{}: {:.3f}%'.format(x, a[x] * 100.))

#create a histogram with the relative frequencies for every letter
plt.bar(a.keys(), a.values(), color= 'red')
#plt.hist(a.values(), len(a.keys()), color= 'yellow')
plt.show()

#print the elapsed time of the process
print(time.process_time())