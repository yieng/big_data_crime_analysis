import json
import timeit

# read all words with idf stats in idf.txt
tic = timeit.default_timer()
idff = open('idf.txt','r')
for doc in idff:
   idf = json.loads(doc)
idff.close()
toc = timeit.default_timer()
print('idf. Time elapsed: ',toc-tic,' sec')

# read all blobs with tf stats in tf.txt
tic = timeit.default_timer()
tff = open('tf.txt','r')
tf = []
for line in tff:
   tf.append(json.loads(line))
tff.close()
toc = timeit.default_timer()
print('tf. Time elapsed: ',toc-tic,' sec')

# get all distinct words
dwordf = open('dword.txt','r')
for doc in dwordf:
    dword = json.loads(doc)
dwordf.close()

# get original comments
comment = open('cm_original.txt','r')
for doc in comment:
    cm = json.loads(doc)
comment.close()

# calculate tf-idf of each word in each comment
tic = timeit.default_timer()

w = open('tfidf.txt','w')
for i in range(0,len(tf)):
   tfidf = []
   for j in tf[i]:
      m = dword.index(j[0])
      if m>=len(idf):
         break
      tfidf.append((j[0],j[1]*idf[m][1]))
   if m>=len(idf):
     continue
   tfidf = sorted(tfidf,key = lambda x: x[1],reverse=True)[:5]
   w.write(json.dumps([tfidf,cm[i]]))
   w.write('\n')
   toc = timeit.default_timer()
   print('tfidf.',i,' Time elapsed: ',toc-tic,' sec ', (toc-tic)/(i+1))
w.close()
