import numpy as np 

arr1 = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([9,8,7,6,5,4,3,2,1])

print(np.vstack((arr1,arr2)));

print(np.hstack((arr1,arr2)));

print("_"*50);
 
print(np.concatenate((arr1,arr2),axis=0 ))