import json
import timeit

tic = timeit.default_timer()
dwordfile = open('dword.txt','r')
for doc in dwordfile:
   dword = json.loads(doc)
dwordfile.close()
toc = timeit.default_timer()
print('1. Time elapsed: ',toc-tic,' sec')
 
tic = timeit.default_timer()
blobfile = open('blobs.txt','r')
for doc in blobfile:
   blob = json.loads(doc)
blobfile.close()
toc = timeit.default_timer()
print('2. Time elapsed: ',toc-tic,' sec')

tic = timeit.default_timer()
n=0
dwordcount = [0 for i in dword] 
m = len(blob)

for b in blob:
    bb = list(set(b))
    n+=1
    for i in bb:
       dwordcount[dword.index(i)]+=1
    toc = timeit.default_timer()
    print('3. Time elapsed: ',toc-tic,' sec',n,';',(toc-tic)/n)

import math
tic = timeit.default_timer()
w = open('idf.txt','w')
w.write(json.dumps([[i,math.log(float(m)/(1+dwordcount[dword.index(i)]))] for i in dword]))
w.close()
toc = timeit.default_timer()
print('4. Time elapsed: ',toc-tic,' sec')
