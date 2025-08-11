import numpy as np;

arr =np.array([10,20,30,40,50,60,70,80,90])

print(arr);

new_arr = np.insert(arr,1,0,axis=0);
print(new_arr)
print(len(new_arr))