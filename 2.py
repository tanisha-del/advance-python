sentence=input("Enter a sentence: ")
vowels=0
consonants=0
for ch in sentence.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels+=1
        else:
            consonants+=1
reversed_sentence=sentence[::-1]
modified_sentence=sentence.replace(" ","_")
capitalized_sentence=sentence.title()
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Reversed:",reversed_sentence)
print("Spaces replaced:",modified_sentence)
print("Capitalized:",capitalized_sentence)
