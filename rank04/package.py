def package_dependency_solver(packages: dict[str, list[str]]) -> list[str]:
	def is_circular(packages: dict[str, list[str]]) -> bool:
		for p1, d1 in packages.items():
			for p2, d2 in packages.items():
				if p2 in d1 and p1 in d2:
					return True
		return False
			
	
	if not packages:
		return []

	if is_circular(packages):
		return []

	result = []
	for p1, d1 in packages.items():
		if not d1:
			result.append(p1)
	result = sorted(result)

	reset = True
	new_packages_list: list[str] = []
	while reset:
		reset = False
		for p1, d1 in packages.items():
			if set(d1) <= set(result) and p1 not in result:
				new_packages_list.append(p1)
				reset = True
				break
		new_packages_list = sorted(new_packages_list)
		result.extend(new_packages_list)
		new_packages_list.clear()

	return result

# result = ["hola", "que", "tal"]
result = package_dependency_solver({"tal": ["hola", "que"], "que": ["hola"], "hola": []})
print(result)
