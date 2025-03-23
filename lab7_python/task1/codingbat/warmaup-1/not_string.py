def not_string(string):
    if string.startswith("not"):
        return string
    return "not "+string
string=input()
print(not_string(string))
