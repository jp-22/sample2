l1 = [[10, 20, {'A': 100}, {'B': 200}, 50, 60, {80, 90, 70}, {'C': [1, 2, 3, 4, [5, 6, 7, 8]]}]]
print(l1)
l1[0].append({ 'D' : [1,2,3,4]})
print(l1)
l1[0][6].add(100)
l1[0][6].add(90)
print(l1)
l1[0].remove({'B':200})
print(l1)
print(len(l1[0]))
# print(max(l1[0]))
print(l1[0])
print(dir(list))