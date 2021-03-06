def bubble_sort(raw_list):
	length = len(raw_list)
	for index in range(length):
		for i in range(1,length-index):
			if raw_list[i-1]>raw_list[i]:
				raw_list[i],raw_list[i-1] = raw_list[i-1],raw_list[i]
	return raw_list

# Test

data_test = [10,23,1,53,654,54,16,646,65,3155,546,31]
sorted_list = bubble_sort(data_test)
print(sorted_list)
