my_list=eval(input())
if my_list[0] > my_list[-1]:
    print([my_list[0]]*3)
elif my_list[0] < my_list[-1]:
    print([my_list[-1]]*3)

