import numpy as np;

arr= np.array([[11,2,3],
            [1,6,6],
            [8,4,5]])


print(arr);
#row wise when axis =0
print("_"*50);
new_arr = np.insert(arr,1,[4,5,6],axis=0)
print(new_arr)


#column wise when axis =1
print("_"*50)
new_arr1 = np.insert(arr,3,[4,5,6],axis=1)
print(new_arr1)

print("_"*50)
new_arr0 = np.insert(arr,1,[4,5,6],axis=None)
print(new_arr0)



print("_"*50)
