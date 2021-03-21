import numpy as np

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]

c = np.array(a, dtype = np.int8)
print(c, type(c))
print(c.dtype)
print(c.ndim)
print(c.shape)

#indexar
print(c[0][1]) #2
print(c[2][1]) #8

#scling
print(c[1:3,2:3]) #[[6],
                  #[9]]
print(c[1:2,0:2]) #[[4],
                  #[5]]
print(c[:,1]) #[[4],
                  #[5]]                  


