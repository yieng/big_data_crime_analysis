f = open('output7_1.txt','r')
chi = open('chicago_crime_rank.txt','w')
uk = open('uk_crime_rank.txt','w')

for line in f:
  if 'United States' in line:
    chi.write(line)
  else:
    uk.write(line)

f.close()
chi.close()
uk.close()
