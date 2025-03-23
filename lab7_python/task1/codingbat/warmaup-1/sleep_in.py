def sleep_in(weekday,vacation):
    return(not weekday or vacation)
weekday=input()=="True"
vacation=input()=="True"
print(sleep_in(weekday,vacation))

