encoding='utf-8'
import json
import timeit

tic = timeit.default_timer()
f = open('cm_uk.txt','r')
w = open('dword_uk.txt','w')
for line in f:
    tic = timeit.default_timer()
    terms = json.loads(line)
    toc = timeit.default_timer()
    print('Time elapsed: ',toc-tic,' sec')
    tic = timeit.default_timer()
    doc = ' '.join(terms)
    toc = timeit.default_timer()
    print('Time elapsed: ',toc-tic,' sec')
    indiv = doc.split(' ')
    print 'indicator'
    dwords = list(set(indiv))
    w.write(json.dumps(dwords))
f.close()
w.close()
