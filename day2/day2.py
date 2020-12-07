with open('data.txt', 'r') as f:
    ls  = [x for x in f.read().splitlines()]
import re
from collections import Counter
counter = 0
counter2 = 0
for x in ls:
    a,b,c,d = re.match(r'(\d+)-(\d+) (\w): (\w+)', x).groups()
    dd = Counter(d)
    e = dd.get(c, -1)
    if int(a) <= e <=int(b):
        counter+=1
    try:
        p = d[int(a) - 1]
    except:
        p = 0

    try:
        q = d[int(b) - 1]
    except:
        q = 0

    if p == c or q == c:
        if q != c or p != c:
            counter2 += 1 # 299, 340 too low

print("Result 1", counter)
print("Result 2", counter2)
