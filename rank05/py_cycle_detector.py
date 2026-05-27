def cycle_detector(graph: dict[int, list[int]]) -> bool:
	if not graph:
		return False
	try:
		indexes: list[int] = []
		for n in graph:
			indexes.append(n)
		visited = [0]
		for index in indexes:
			l = graph[index]
			visited_now = []
			for n in l:
				for n_ in graph[n]:
					if n_ in visited:
						return True
				visited_now.append(n)
			visited.extend(visited_now)
			visited_now.clear()
		return False
	except Exception:
		return False

print(cycle_detector({0: [1], 1: [2], 2: [3], 3: [0]}))
print(cycle_detector({0: [1, 2], 1: [3], 2: [3], 3: []}))
