if __name__=="__main__":
    xiao = 1
    zhong = 0
    da = 0
    sum = xiao+zhong+da
    i = 1
    while i<=30:
        print(f"第{i}个月的兔子数",sum)
        i = i+1
        da = zhong +da
        zhong = xiao
        xiao = da
        sum = xiao + zhong + da


