import numpy as np 

arr=np.array([1,1,1,np.nan,9,8,np.nan,7])
print(np.isnan(arr));

print("_"*50)

cleaned_arr = np.nan_to_num(arr,nan=5)
print(cleaned_arr);

print("_"*50)

arr = np.array([1,2,3,np.inf,7,np.nan ,4,5,np.inf])

cleaned_arr2 = np.nan_to_num(arr,posinf=500,neginf=500,nan=50)

print(cleaned_arr2)