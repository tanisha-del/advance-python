s=input("Enter string: ")
vowels=0
consonants=0
digits=0
special=0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Digits:",digits)
print("Special:",special)
