import random


array = [random.randint(-100, 100) for i in range(10)]
print(array)
minim = array[0]
maxim = array[1]
for i, item in enumerate(array):
	if array[i] < minim:
		minim = array[i]
	if array[i] > maxim:
		maxim = array[i]

print(minim, maxim)

minx = 0
maxx = 0

for i, item in enumerate(array):
	if array[i] == minim:
		minx = i
	if array[i] == maxim:
		maxx = i

print(minx, maxx)
array[minx], array[maxx] = array[maxx], array[minx]
print(array)
