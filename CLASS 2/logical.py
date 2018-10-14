a= 1
b= 1

print("AND:", a and b)
print("or", a or b)
print("Not :", not a)

a=(4,5,7,6,78,8)
if 4 in a:
    print("found")
if 2 not in a:
    print("not found")

a=5
b=5
if a is b:
    print("Same")
b=6
if a is not b:
    print("different")
