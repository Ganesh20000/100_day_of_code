import numpy as np 

arr = np.array([1,2,3,np.nan,4,5,np.nan])

updated_arr =  np.nan_to_num(arr)

print(updated_arr)
print("_"*50)
u2 = np.nan_to_num(arr,nan=8);

print(u2)

