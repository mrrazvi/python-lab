import numpy as np

# 0d - scalar

a = np.array(4)

print(a)
print(a.ndim)

# 1d - vector

b = np.array([1, 2, 3, 4, 5])

print(b)
print(b.ndim)

# 2d - matrix

c = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
])

print(c)
print(c.ndim)

# 3d - tensor

d = np.array([
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0]
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0]
    ],
])

print(d)
print(d.ndim)
