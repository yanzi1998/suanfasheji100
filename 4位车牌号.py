def chepai():
    for i in range(10):
        for j in range(10):
            if i != j:
                a = i*1000+i*100+j*10+j
                for b in range(31,100):
                    if b*b ==a:
                        return a

print(chepai())



