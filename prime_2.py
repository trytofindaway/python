p = [True]*100
p[0] = False
p[1] = False
n = 2


def chart():
    s = ""
    for i in range(100):
        if p[i] == True:
            s += "{:2d}, ".format(i)
        else:
            s += "／, "
        if i % 10 == 9:
            s += "\n"
    print(s)


def furui():
    global n
    for i in range(n + n, 100, n):
        p[i] = False
        print(n, "の倍数をふるい落としました")
        chart()
        while n < 100:
            n = n + 1
            if p[n] == True:
                break


chart()
while n < 10:
    input("Enterキーを押してください")
    furui()
