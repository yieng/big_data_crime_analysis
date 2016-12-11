w = open("output4_1.txt","w")
path = [
    "output2.txt", "output3.txt"
    ]
for i in range(0,len(path)):
    f = open(path[i], "r")
    for line in f:
        if i==0:
            if len(line.split(",")) >= 6:
                entry = line.split(",",4)
                entry = [','.join(entry[0:4])]
            else:
                entry = line.rsplit(",",1)
        else:
            if len(line.split(",")) >= 6:
                entry = line.split(",",5)
                entry = [','.join(entry[0:5])]
            else:
                entry = line.rsplit(",",1)
        w.write(entry[0]+"\n")
    f.close()
w.close()
