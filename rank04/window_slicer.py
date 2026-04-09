def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
	if not nums:
		return []

	if k <= 0 or k > len(nums):
		return []

	result = []
	for i in range(len(nums) - k + 1):
		maximum = nums[i]
		for j in range(i, i + k):
			if maximum < nums[j]:
				maximum = nums[j]
		result.append(maximum)
	return result


l = [1, 2, 3, 4, 5]
size = 3
result = sliding_window_maximum(l, size)
print(result)