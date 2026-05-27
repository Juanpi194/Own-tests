def spiral_no_se_que(size: int) -> list[list[int]]:
	matrix: list[list[int]] = []
	for y in range(size):
		matrix.append([])
		for x in range(size):
			matrix[y].append(0)
	
	y = 0
	x = 0
	count = 1
	while count < size * size + 1:
		while x <= size - 1 and count < size * size + 1:
			matrix[y][x] = count
			count += 1
			if x == size - 1 or matrix[y][x + 1] != 0:
				y += 1
				break
			x += 1
		
		while y <= size - 1 and count < size * size + 1:
			matrix[y][x] = count
			count += 1
			if y == size - 1 or matrix[y + 1][x] != 0:
				x -= 1
				break
			y += 1

		while x >= 0 and count < size * size + 1:
			matrix[y][x] = count
			count += 1
			if x == 0 or matrix[y][x - 1] != 0:
				y -= 1
				break
			x -= 1

		while y >= 0 and count < size * size + 1:
			matrix[y][x] = count
			count += 1
			if y == 0 or matrix[y - 1][x] != 0:
				x += 1
				break
			y -= 1
	return matrix


print(spiral_no_se_que(3))
print(spiral_no_se_que(4))
