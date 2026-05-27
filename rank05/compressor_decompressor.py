def compressor_decompressor(data: str, operation: str) -> str:
	def compress(s :str) -> str:
		last_c = s[0]
		count = 0
		result = ""
		for c in s:
			if c == last_c:
				count += 1
				if count == 10:
					result += f"{last_c}{9}"
					count = 1
			else:
				result += f"{last_c}{count}"
				count = 1
				last_c = c
		result += f"{last_c}{count}" if count > 1 else last_c
		return result


	def decompress(s: str) -> str:
		...

	if not data:
		return ""
	if operation != "compress" and operation != "decompress":
		return "Error"
	if operation == "compress":
		return compress(data)
	return decompress(data)



print(compressor_decompressor("aaabbc", "compress"))
# aaaaaaaaaaaaaa -> a9a4 
# aaabbc -> a3b2c
# b2c2 -> bbcc
