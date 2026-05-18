def palindrome_obtainer(list: list[str]) -> list[str]:
	result = []
	if not list:
		return []
	for s in list:
		if s.lower() == s.lower()[::-1]:
			result.append(s)
	return sorted(result)

list = ["radar", "casa", "oso", "perro", "Ana", "sol"]
result = palindrome_obtainer(list)
print(result)
