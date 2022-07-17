l1 = ['dfhsu','fhgoufh','wuhr']
print(l1[0])
l2 = [89,38]
l1 +=l2
print(l1)

import time
result = []
start = time.time()
for i in range(10000):
    result.insert(0,i)

print('操作执行',len(result),'次，用时',time.time()-start)

result2 = []
start = time.time()
for i in range(10000):
    result2.append(i)
print('操作执行',len(result),'次，用时',time.time()-start)

result3 = []
start = time.time()
for i in range(10000):
    result3 = result3+[i]
print('操作执行',len(result),'次，用时',time.time()-start)

result3 = []
start = time.time()
for i in range(10000):
    result3 +=[i]
print('操作执行',len(result),'次，用时',time.time()-start)
