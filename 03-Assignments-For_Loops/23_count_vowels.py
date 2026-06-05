# 23. Given: text = "python programming" 
# Goal: Count how many vowels are in the string. 
# Constraint: Do not use indexing (text[i]) or slicing (text[:]). 
text = "python programming"
count = 0
for i in text:
    # print(i)
    if i in "aeiou":
        count+=1
print(count)