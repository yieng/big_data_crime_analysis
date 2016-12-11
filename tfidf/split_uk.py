import json
import timeit
cm = []

tic = timeit.default_timer()
f = open('cm_uk.txt','r')
for line in f:
    terms = json.loads(line)
    for i in range(0,len(terms)):
        terms[i] = terms[i].split(' ')
        while '' in terms[i]:
            terms[i].remove('')
        cm.append(terms[i])
        toc = timeit.default_timer()
        print(i, '\tTime elapsed: ',toc-tic,' sec')
f.close()

w = open('blobs_uk.txt','w')
w.write(json.dumps(cm))
w.close()
