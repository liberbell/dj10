s = "django"

print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print((s[-2:]))

l = [3, 7, [1, 4, "hello"]]
print(l)
l[2][2] = "goodbye"
print(l)

d1 = {"simple_key": "hello"}
d2 = {"k1": {"k2": "hello"}}
d3 = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}

mylist = [1,1,1,2,2,2,2,3,3,3]
converted = set(mylist)
print(converted)

age = 4
name = "sammy"
print("Hello my dog`s name is {} and he is {} years old.".format(name, age))