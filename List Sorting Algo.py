# List sorting algorithm:
input_list = [87, 45, 12, 5, 47, 85, 12, 16, 51, 57, 74, 43, 17, 55, 2, 0, 1, 19, 64, 75, 88, 99, 4, 5, 63, 6, 76, 7, 10, 23, 0]

def sorting(x):
	sorted_list=[]
	total=len(x)
	while len(sorted_list)<total:
		sorted_list.append(min(x))
		x.remove(min(x))
	return sorted_list

print(sorting(input_list))