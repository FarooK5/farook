lst=[10,11,12,13,15,15,16,15]
st=set(lst)
print(st)

st1={1,2,3,7,10}
st2={4,2,10,12,15}
set_union=st1.union(st2)
print(set_union)

intersection_set=st1.intersection(st2)
print(intersection_set)


diff_set=st1.difference(st2)
print(diff_set)

students={"ram","ravi","hari","tom","nikhil","jain","jhon"}
passed_students={"ravi","hari","tom"}
failed_students=students-(passed_students)
print(failed_students)