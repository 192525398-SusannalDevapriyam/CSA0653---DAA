def string_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            return i

    return -1


text = "ABCDE"
pattern = "DE"

result = string_match(text, pattern)

print("Text:", text)
print("Pattern:", pattern)

if result != -1:
    print("Pattern found at index", result)
else:
    print("Pattern not found")

input("press enter to exit...")
