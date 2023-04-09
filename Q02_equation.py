def equation(a, b, c):
    result =  (a+b+c) * (a-b-c) * a*b + a**2 + b ** 2 + (a*b*c)**3
    # section_a = (a + b + c) * (a - b - c) * a * b
    # section_b = a ** 2 + b ** 2
    # section_c = (a * b * c) ** 3
    # return section_a + section_b + section_c
    return result
print(equation(2,3,4))




