# # using for loop


prices = [100, 200, 300, 400, 500, 600,700,800,900,1000,1321,45,485,88,555,99,500,444,88]

d = 10

final_prices = []

for price in prices:
    final_price = price - (price * d/100);
    final_prices.append(final_price)

print(final_prices)


print("_"*50)

import numpy as np
pri = np.array([100, 200, 300, 400, 500, 600,700,800,900,1000,1321,45,485,88,555,99,500,444,88])

dis =10

final = pri- (pri*dis/100);
print(final)


