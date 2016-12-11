import json
import timeit

tic = timeit.default_timer()
f = open('tfidf.txt','r')
cm = []
for d in f:
    cm.append(json.loads(d))
f.close()
toc = timeit.default_timer()
print('read. Time elapsed: ',toc-tic,' sec')

kw = ['weapon','weapons','shoplifting','shoplift', 'arson',
      'damage', 'gun', 'firearm', 'criminal', 'drug', 'vehicle',
      'unlawful', 'crime', 'solicitation', 'theft', 'abuse',
      'sexual', 'rape', 'ammunition', 'violation', 'offense',
      'hijack', 'firearm', 'coin-op', 'peeping']

pl = ['chicago','illinois']

tic = timeit.default_timer()
for k in kw:
    for p in pl:
        w = open(k+'_'+p+'.txt','w')
        n=0
        for c in cm:
            n+=1
            terms = []
            for i in range(0,5):
                terms.append(c[0][i][0])
            if (k in terms) and (p in terms):
                w.write(json.dumps(c))
                w.write('\n')
                toc = timeit.default_timer()
                print(n,' Time elapsed: ',toc-tic,' sec')
    w.close()
