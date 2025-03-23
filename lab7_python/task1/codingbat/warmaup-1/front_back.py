string=input()
string_list=list(string)

string_list[0],string_list[-1]=string_list[-1],string_list[0]
new_string="".join(string_list)
print(new_string)