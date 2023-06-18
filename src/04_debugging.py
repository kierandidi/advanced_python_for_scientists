import numpy as np

#write some code
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
print(c)

x=0

for i in range(5):
    print(x)
    x += 1
    c += b

#write a more complex function
def my_func(a,b):
    c = a + b
    return c    

def run_my_func():
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    c = my_func(a,b)
    print(c)

run_my_func()