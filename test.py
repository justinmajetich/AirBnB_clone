
s = "enimA"

print(s[::-1])

s = "AiiA"

def isPalind(s):
    for i in range(len(s)):
        if (s[i] != s[len(s) - i - 1]):
            return print("Not Palindrom")
            
    return print("Is Palindrom")

isPalind(s)