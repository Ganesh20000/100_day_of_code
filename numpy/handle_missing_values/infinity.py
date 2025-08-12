import numpy as np 

arr =([1,2,3,np.inf, 4,-np.inf,7,np.inf,9,np.inf])

print(np.isinf(arr))

print("_"*50)
arr_2 = np.nan_to_num(arr,posinf=11,neginf=44)
print(arr_2)
