def xyz_there(s):
    return ".xyz" not in s.replace("xyz", "_xyz")
s=input()
print(xyz_there(s))
