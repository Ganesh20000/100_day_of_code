import numpy as np

val= np.arange(12)
print(val)


arr = val.reshape((3,4))
print(arr);



print(val[2:7])

print("with step",val[0:10:2])


print("negative indexing", val[::-1])


print