w = open("output5_1.txt","w")
path = [
    "output4_1.txt"
    ]
for i in range(0,len(path)):
    f = open(path[i], "r")
    for line in f:
        w.write("1;"+line)
    f.close()
w.close()
