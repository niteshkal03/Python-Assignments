# 24. Given: text = "programming" 
# Goal: Print all characters that repeat in the string. 
text = "programming"
repeat = " "
for i in text:
    repeat+= i
    if i == repeat:
        print(i)
