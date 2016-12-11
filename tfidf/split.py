import json
import timeit
cm = []

tic = timeit.default_timer()
f = open('cm.txt','r')

for line in f:
    comment = json.loads(line)
    terms = comment
    for i in range(0,len(comment)):
        terms[i] = comment[i].split(' ')
        while '' in terms[i]:
            terms[i].remove('')
        cm.append(terms[i])
        toc = timeit.default_timer()
        print(i, '\tTime elapsed: ',toc-tic,' sec')
f.close()

w = open('blobs.txt','w')
w.write(json.dumps(cm))
w.close()
