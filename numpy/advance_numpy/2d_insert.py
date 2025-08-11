import numpy as np;

arr= np.array([[11,2,3],
            [1,6,6],
            [8,4,5]])


print(arr);

print("_"*50);
new_arr = np.insert(arr,1,[4,5,6],axis=0)
print(new_arr)

print("_"*50)
new_arr = np.insert(arr,1,[4,5,6],axis=2)
print(new_arr)

print("_"*50)
new_arr = np.insert(arr,1,[4,5,6],axis=2)
print(new_arr)



print("_"*50)
new_arr = np.insert(arr,1,[4,5,6],axis=None)
print(new_arr)
