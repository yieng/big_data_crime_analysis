import dstk
dstk = dstk.DSTK()

coord=[]
typecrime=[]
path = [
    "Chicago_Crimes_2016_AugSep.csv"
    ]
for i in range(0,len(path)):
    f = open(path[i], "r")
    for line in f:
        entry = line.rsplit(',')
        if entry[-1]=='Location' or entry[-4]=="Updated On" or entry[-4]=='' or entry[-3]=='':
            continue
        else:
            coord.append([float(entry[-4]),float(entry[-3])])
            typecrime.append(entry[5])
    f.close()
#extract coordinates
###

f = open("output3.txt","w")
for i in range(0,len(coord)):
    f.write(typecrime[i]+": ")
    address = dstk.coordinates2politics(coord[i])
    level = address[0]['politics']
    if level==None:
        f.write("\n")
        continue
    else:
        for j in range(0,len(level)):
            f.write(level[j]['name'])
            if j!=len(level)-1:
                f.write(", ")
    f.write("\n")
f.close()
