arr1=[11,12,13,14,15]
arr2=[12,13,15,16,18]
arr1.sort()
arr2.sort()
p1=0
p2=0
while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(f"common number is {arr1[p1]}")
        p1+=1
        p2+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
        jhghhj