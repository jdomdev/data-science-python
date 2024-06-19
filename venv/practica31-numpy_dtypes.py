# A Comprehensive Guide to NumPy Data Types
# What else is out there besides int32 and float64?

import numpy as np
print(np.__version__) # test


# 1.INTEGERS
# ----------


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
import numpy as np
with np.errstate(over='raise'):
    print(np.array([2**31-1])[0]+1)
# FloatingPointError: overflow encountered in scalar add

with np.errstate(over='ignore'):
    print(np.array([2**31-1])[0]+1)
# -2147483648

a = np.array([10], dtype=object)
len(str(a**1000))
# 1003


# 2. FLOATS
# ---------


x = np.array([-1234.5])
1/(1+np.exp(-x))
# <stdin>:1: RuntimeWarning: overflow encountered in exp
# array([0.])

np.exp(np.array([1234.5]))
# array([inf])

x = np.array([-1234.5], dtype=np.float128)
1/(1+np.exp(-x))
# array([0.]) # -> float128: no disponible en Windows

9279945539648888.0+1
# = 9279945539648888.0

len('9279945539648888')
# = 16

from decimal import Decimal as D
a = np.array([D('0.1'), D('0.2')]); a
# = array([Decimal('0.1'), Decimal('0.2')], dtype=object)
a.sum()
# = Decimal('0.3')

from fractions import Fraction
a = np.array([Fraction(1, 10), Fraction(1, 5)], dtype=object)
# = a = np.array([Fraction(1, 10), Fraction(1, 5)], dtype=object)
a.sum()
# = Fraction(3, 10)

np.array([1+2j])
# = array([1.+2.j])

a = np.array([np.nan, 5, np.nan, 5, 5])
a[~np.isnan(a)].mean()
# = 5.0


# 3. BOOLS
# --------

import sys
sys.getsizeof(True)
# = 28


# 4. CADENAS
# ----------


np.array(['abcde', 'x', 'y', 'x'])
# = array(['abcde', 'x', 'y', 'x'], dtype='<U5')












