import json
import timeit

encoding='utf-8'

path = ['part-00000chi.txt','part-00001chi.txt','part-00002chi.txt']

cm = []

n=0
tic = timeit.default_timer()
for file in path:
   f = open(file, 'r')
   for doc in f:
      n+=1
      d = doc.lower()
      for char in '?.,!/;:\\\'\"*^0123456789':
          d = d.replace(char,'')
      for char in '()[]{}':
          d = d.replace(char,' ')
      cm.append(d)
      toc = timeit.default_timer()
      print('n = ',n," and time: ",toc-tic)
   f.close()


f = open('cm.txt','w')
f.write(json.dumps(cm))
f.close()

path = ['part-00000uk.txt','part-00001uk.txt','part-00002uk.txt']

cm = []

n=0
tic = timeit.default_timer()
for file in path:
   f = open(file, 'r')
   for doc in f:
      n+=1
      d = doc.lower()
      for char in '?.,!/;:\\\'\"*^0123456789':
          d = d.replace(char,'')
      for char in '()[]{}':
          d = d.replace(char,' ')
      cm.append(d)
      toc = timeit.default_timer()
      print('n = ',n," and time: ",toc-tic)
   f.close()


f = open('cm_uk.txt','w')
f.write(json.dumps(cm))
f.close()
