# 27. Give : text=”if you think you can not do, you can not show think wisely”  
# Goal: Print the alternate words  
# Constraint: Do not use space between words more than once . 
text="if you think you can not do, you can not show think wisely"
size = len(text)
space = " "
for i in range(1,size,2):
    if i == "  ":
        space = space - i
    print(text[i], end=" ")
    # print(text[i], end=" ")
