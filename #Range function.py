#Range function

#range(<starting index>, <last index>, step size)
#starting index is included
#ending index is not included in the range

for number in range(1,11, 2):
    print(number)
    
sum_num = 0

for number in range(1,101):
    sum_num += number

print(sum_num)