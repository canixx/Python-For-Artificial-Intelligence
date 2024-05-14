try:
    1/1
except:
    print("except")
else:
    print("else")
finally:
    print("done")



try:
    1/0
except:
    print("except")
else:
    print("else")
finally:
    print("done")

a = {"x":2,"y":3}

b = dict(zip(a.values(),a.keys()))
print(b)

a = [1,2,3]

for i in a:

    i+1

print(a)

print(sum([1,2,3]))

c = 1

while True:

    if c % 3 == 0:

        break

    print(c)

    c = c + 1

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a*b
d = np.dot(a,b)










