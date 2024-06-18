# A Comprehensive Guide to NumPy Data Types
# What else is out there besides int32 and float64?
import numpy as np
print(np.__version__) # test

# 1.Integers

np.array([1,2,3]).dtype
# dtype('int32')

np.arange(10**6)
# array([     0,      1,      2, ..., 999997, 999998, 999999])
np.arange(10**6).reshape(1000, 1000)
'''
array([[     0,      1,      2, ...,    997,    998,    999],
       [  1000,   1001,   1002, ...,   1997,   1998,   1999],
       [  2000,   2001,   2002, ...,   2997,   2998,   2999],
       ...,
       [997000, 997001, 997002, ..., 997997, 997998, 997999],
       [998000, 998001, 998002, ..., 998997, 998998, 998999],
       [999000, 999001, 999002, ..., 999997, 999998, 999999]])
'''

np.array([255], np.uint8) + 1
# array([0], dtype=uint8)

np.array([2**31-1])
# array([2147483647])

np.array([2**31-1]) + 1
# array([-2147483648])

np.array([2**63-1]) + 1
# array([-9223372036854775808], dtype=int64)

np.array([255], np.uint8)[0] + 1
# 256

np.array([2**31-1])[0] + 1
# -2147483648

np.array([2**63-1])[0] + 1
# <stdin>:1: RuntimeWarning: overflow encountered in scalar add
# -9223372036854775808

with np.errstate(over='raise'):
    print(np.array([2**31-1])[0]+1)
# FloatingPointError: overflow encountered in scalar add

with np.errstate(over='ignore'):
    print(np.array([2**31-1])[0]+1)
# -2147483648

# Página 6 >>>