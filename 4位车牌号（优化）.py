if __name__=="__main__":
    flog = 0
    for i in range(10):
        if flog:
            break
        for j in range(10):
            if flog:
                break
            if i != j:
                a = i*1000+i*100+j*10+j
                for b in range(31,100):
                    if b*b ==a:
                        print('车牌号为：',a)
                        flog = 1
                        break


