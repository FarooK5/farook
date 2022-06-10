# lst=[10,11,12,13,14,15,16]
# element=1
# flag=0
# for num in lst:
#     if element==num:
#         flag=1
#         break
# print("element found" if flag==1 else "not found")
lst=[10,11,12,15,1,100,20]
evenlist=[]
for num in lst:
    if num%2==0:
        evenlist.append(num)
print(evenlist)
evenlist.sort(reverse=True)
print(evenlist)