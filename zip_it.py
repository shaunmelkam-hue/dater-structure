sp1 = {1, 2, 3,}
sp2 = {'a', 'b', 'c'}
s3 = list(zip(sp1, sp2))
print(s3,"\n")

list1 = [10, 20, 30]
list2 = [ 100, 200, 300]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

stocks = {'reliance', 'infosys', 'tcs',}
price = {2175, 1127, 2750}

new_dict = {stocks: price for stocks,
             price in zip(stocks, price)}
print('\n{}'.format(new_dict))