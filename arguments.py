def add_numbers(*args):
    total=0
    for num in args:
        total=total+num
    return num

total=add_numbers(1,2,3,45)
print(total)    


#  *args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed. 