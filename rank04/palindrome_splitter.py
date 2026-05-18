# NI IDEA JULIO
def palindrome_splitter(s: str) -> int:
	def is_palindrome(s: str) -> bool:
		if s == s[::-1]:
			return True
		return False

	count = 0
	i = 0
	j = len(s)
	while i < len(s):
		if is_palindrome(s[i:j]):
			count += 1
			i = j
			j = len(s)
		else:
			j -= 1
	return count - 1

s1 = "abcd"
s2 = "aabaa"
s3 = "aab"
result1 = palindrome_splitter(s1)
result2 = palindrome_splitter(s2)
result3 = palindrome_splitter(s3)
print(result1)
print(result2)
print(result3)

"""
aab -> aa | b
aabaa -> aabaa
abcd -> a | b | c | d
"""
