def merge_sorted_list(lists: list[list[int]]) -> list[int]:
	new_list = []

	if not lists:
		return []
	
	for l in lists:
		if l:
			new_list.extend(l)
	new_list.sort()
	return new_list

result = merge_sorted_list([[1, -3, 5], [2, 4, 6], [-4, -5, 6]])
print(result)
