def monkey_trouble(a_smile, b_smile):
    return not(a_smile^b_smile)
a_smile=input()=="True"
b_smile=input()=="True"
print(monkey_trouble(a_smile, b_smile))