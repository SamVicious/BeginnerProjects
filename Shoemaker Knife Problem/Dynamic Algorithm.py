import math
num_of_people = int(input())
people_list = [x for x in range(1, num_of_people + 1)]
while len(people_list) != 1:
	i = 0
	for x in range(int(math.ceil(len(people_list) / 2))):
		if i == len(people_list) - 1:
			people_list.pop(0)
		else:
			people_list.pop(i + 1)
			i += 1
print(people_list)