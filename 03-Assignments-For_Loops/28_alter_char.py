# 28. Given: text = "knowyourself" 
# Goal: Find and print the alternate characters.
#  
text = "knowyourself"
size = len(text)
for i in range(1,size,2):
    print(text[i], end=" ")
    
