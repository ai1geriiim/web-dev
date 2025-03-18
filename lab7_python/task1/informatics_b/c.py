test_number=int(input())
boy_number=int(input())
if (test_number > 1 or test_number < 1) and (boy_number > 1 or boy_number < 1):
    print("YES")
elif (test_number == 1) and (boy_number > 1 or boy_number <1):
    print("NO")
elif (test_number == boy_number):
    print("YES")
else:
    print("NO")
