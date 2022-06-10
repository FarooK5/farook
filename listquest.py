lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]
# for sub_lst in lst:
#     for num in sub_lst:
#         if num>=15:
#              print(num)
#
# print(lst)
# flatten_lst=[]
# for sub_lst in lst:
#     for num in sub_lst:
#         flatten_lst.append(num)
# print(max(flatten_lst))

flatten_list=[num for sub_lst in lst for num in sub_lst]
print(flatten_list)


numgrtsix=[num for num in flatten_list if num>16]
print(numgrtsix)
#
odd=[num for num in flatten_list if num%2!=0]
print(f"odd numbers {odd}")

evensum=[num for num in flatten_list if num%2==0]
print(sum(evensum))

mapping=[num+1 if num>25 else num-1 for num in flatten_list]
print(mapping)
