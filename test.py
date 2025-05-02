# print(range(0,10), type(range(0,10)),dict(range(0,10)))
d1 = dict()
for item in range(10):
    d1[item] = item

print(d1)
print(d1.keys())
print(d1.values())