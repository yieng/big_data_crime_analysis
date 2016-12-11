crime = []

path = [
    "output6_1.txt"
    ]
for i in range(0,len(path)):
    f = open(path[i], "r")
    for line in f:
        entry = line.split(";")
        crime.append((int(entry[0]),entry[1]))

sortedcrime = sorted(crime, reverse=True)

w = open("output7_1.txt","w")
for i in range(0,len(sortedcrime)):
    w.write(str(sortedcrime[i][0])+";"+sortedcrime[i][1])
w.close()
