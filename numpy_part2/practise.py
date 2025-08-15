import numpy as np

import numpy as np
import matplotlib.pyplot as plt
# res_id , 2021,2022,2023,2024
sales = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 110000, 135000, 150000, 170000],  # Burger Shack
    [5, 175000, 185000, 210000, 240000],  # Curry Palace
])


print(sales)

# print(sales)
print(sales.shape)
print(sales.size)
print("_"*50)
print(sales[0:3]) or print(sales[:3])
print("_"*50)

print(sales[:,:2])



# in sum  column axis =0 and row axis =1
# axis 1  means row here
print(np.sum(sales,axis=1))

# axis 0 means column here
print(sum(sales))
yearly_sales =np.sum(sales[:,1:],axis=0) # column sum exclude id 
print(yearly_sales)

#minimum sale per year 
# row wise
mini_per_res = np.min(sales[:,1:],axis=1)
print("\n mini sale per year",mini_per_res)
print("_"*50)


#maximum sales per year

max_sale_per_year = np.max(sales[:,1:],axis=0)
print("\n max sale per year",max_sale_per_year)


print("_"*50)
average_sale_per_res = np.mean(sales[:,1:],axis=1)
print("\n average sale pear res",average_sale_per_res)

print("_"*50)
cumsum = np.cumsum(sales[:,1:],axis=1)
print("\n cumsum saler per ", cumsum)

print("_"*50)
# plt.figure(figsize=(6,6))
# plt.plot(np.mean(cumsum,axis=0))
# plt.title("average cumsum sale accorss all restrant")
# plt.xlabel("years")
# plt.ylabel("sales")
# plt.grid(True)
# plt.show()

# print("_"*50)

vector1 =np.array([1,2,3,4,5,])
vector2 = np.array([6,7,8,9,10])


print("\n addition of vector ",vector1+vector1)

print("_"*50)
print("multiplication of vector ", vector1*vector2)


print("dot product of vector ", np.dot(vector2,vector1))

print("_"*50)

#Montly avg
#broadcasting

month_avg = np.array(sales[:,1:]/12)
print(month_avg)
print("_"*50)

#increment 
increment = month_avg+500
yearly_inc = increment*12
print(yearly_inc)
