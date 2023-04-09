x = "89e9jcd^o38829@3%3,/mkl$w1"
numbers = ''.join(filter(str.isdigit, x))
print(numbers)


import re

x = "89e9jcd^o38829@3%3,/mkl$w1"
numbers = re.findall(r'\d+', x)
print(''.join(numbers))




x = "89e9jcd^o38829@3%3,/mkl$w1"
numbers = re.sub('[^0-9]', '', x)
print(numbers)

