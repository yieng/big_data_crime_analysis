w = open("output2.txt","w")
path = [
    "output2a1.txt", "output2a2.txt", "output2a3.txt", "output2a4.txt", "output2b1.txt", "output2b2.txt", "output2b3.txt", "output2b4.txt", "output2c1.txt", "output2c2.txt", "output2c3.txt", "output2c4.txt", "output2d1.txt", "output2d2.txt", "output2d3.txt", "output2d4.txt", "output2e1.txt", "output2e2.txt", "output2e3.txt", "output2e4.txt", "output2f.txt", "output2g.txt", "output2g2.txt", "output2g3.txt", "output2g4.txt", "output2h.txt", "output2i.txt", "output2j.txt", "output2k.txt", "output2l1.txt", "output2l2.txt", "output2l3.txt", "output2l4.txt", "output2m1.txt", "output2m2.txt", "output2m3.txt", "output2m4.txt", "output2n.txt", "output2o.txt", "output2p1.txt", "output2p2.txt", "output2p3.txt", "output2p4.txt", "output2q.txt", "output2r.txt", "output2r1.txt", "output2s.txt", "output2t1.txt", "output2t2.txt", "output2t3.txt", "output2t4.txt", "output2u1.txt", "output2u2.txt", "output2u3.txt", "output2u4.txt", "output2v.txt"
    ]
for i in range(0,len(path)):
    f = open(path[i], "r")
    for line in f:
        w.write(line)
    f.close()
w.close()
