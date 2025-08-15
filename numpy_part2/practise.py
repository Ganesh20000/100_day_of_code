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

 
