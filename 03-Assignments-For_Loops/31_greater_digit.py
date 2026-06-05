# 31.Count how many digits in the string are greater than 5 from text = "1234567890". 
text = "1234567890"
for i in text:
    sum1 = 0
    convert_int = int(i)
    if convert_int > 5:
        sum1+=convert_int
        print(sum1)