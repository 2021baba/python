
item=['Fruit','Books','Others']
prices=[96,97,98]
#以少的为准
d={item:price for item,price in zip(item,prices)}
print(d)

