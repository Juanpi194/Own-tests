def intersection_finder(lists: list[list[int]]) -> list[int]:
	result = []
	for x in lists[0]:
		if all(x in l for l in lists):
			if x not in result:
				result.append(x)
	return result


result = intersection_finder([[1, 2, 3], [2, 4, 6], [1, 4, 7, 2], [3, 1, 4, 2]])
print(result)
