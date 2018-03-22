def insertion_list(list):
	for index in range(1, len(list)):
		value = list[index]
		i = index - 1
		while i >= 0:
			if value < list[i]:
				list[i+1] = list[i]  #shift number in slot i right to slot i+1
				list[i] = value  #shift value left into slot i.
				i = i - 1
			else:
				break
	return list

liste = [99,1,2,46,777,885,53,7,84]

print(insertion_list(liste))