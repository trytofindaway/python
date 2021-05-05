for i in range(1,10):
    k = ""
    for j in range(1,10):
        k = k + "{}x{}={:2d} ".format(j,i,i*j)
        print(k)

        print("ゼロ詰め {:010d}".format(123))
        print("十六進法 {:04x}".format(256))
        print("二進法 {:08b}".format(3))