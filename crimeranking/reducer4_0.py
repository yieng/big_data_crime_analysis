crime = []
count = []

path = [
    "output5_1.txt"
    ]
for i in range(0,len(path)):
    f = open(path[i], "r")
    for line in f:
        entry = line.split(";")
        if (entry[1] not in crime):
            crime.append(entry[1])
            count.append(0)
            count[crime.index(entry[1])]+=int(entry[0])
            print(crime.index(entry[1]))
        else:
            count[crime.index(entry[1])]+=int(entry[0])

w = open("output6_1.txt","w")
for i in range(0,len(crime)):
    w.write(str(count[i])+";"+crime[i])
w.close()
