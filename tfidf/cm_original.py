import json
import timeit

encoding='utf-8'

path = ['part-00000chi.txt','part-00001chi.txt','part-00002chi.txt']

cm = []

n=0
tic = timeit.default_timer()
for file in path:
   f = open(file, 'r')
   for d in f:
      n+=1
      cm.append(d)
      toc = timeit.default_timer()
      print('n = ',n," and time: ",toc-tic)
   f.close()


f = open('cm_original.txt','w')
f.write(json.dumps(cm))
f.close()

path = ['part-00000uk.txt','part-00001uk.txt','part-00002uk.txt']

cm = []

n=0
tic = timeit.default_timer()
for file in path:
   f = open(file, 'r')
   for d in f:
      n+=1
      cm.append(d)
      toc = timeit.default_timer()
      print('n = ',n," and time: ",toc-tic)
   f.close()


f = open('cm_original_uk.txt','w')
f.write(json.dumps(cm))
f.close()
