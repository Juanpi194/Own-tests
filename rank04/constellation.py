def draw_constellation(stars: list[tuple[int, int]], size: int) -> list[str]:
	result = []
	for y in range(size):
		result.append("")
		for x in range(size):
			if (x, y) in stars:
				result[y] += "*"
			else:
				result[y] += "."
	return result


result = draw_constellation([(0, 0), (1, 1), (2, 2)], 4)
for line in result:
	print(line)
