s=input("Enter sentence: ")
freq={}
for ch in s:
    if ch.isalnum():
        freq[ch]=freq.get(ch,0)+1
for ch in freq:
    if freq[ch]==1:
        print(ch,end=" ")
