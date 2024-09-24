def schreder ():
    for i in range (1000,10000):
        lastwo = i % 100
        firstwo = i // 100
        if firstwo**2 + lastwo**2 == i:
            print (i)

schreder()