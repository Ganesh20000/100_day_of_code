import numpy as np


arr1 = np.array([1,2,3,4,5,6,7,8,9])

arr2 = np.array([10,20,30,40,50,60,70,80,90])
arr2_a = np.append(arr2,[11,22,33])

con= np.concatenate((arr1,arr2_a),axis=0)
print(con);

print(len(con));