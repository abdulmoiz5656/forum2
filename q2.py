stock = {
 "banana":6,
 "apple":0,
 "orange":32,
 "pear":15}
prices = {
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3}
for key in prices.keys():
    print(key)
    print("price is :", (prices[key]))
    print("stock is :", (stock[key]))

total = 0
for key in prices.keys():
    total += (prices[key]*stock[key])
print(total)