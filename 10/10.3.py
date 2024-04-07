#wap a numpy program to genrate random num from 10 to 30

import numpy  as np
def rand():
 return np.random.randint(9, 31)

for i in range(5):
    print(rand())
    