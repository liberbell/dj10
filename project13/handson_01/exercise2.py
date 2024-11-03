def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))

def stringBits(mystring):

    result = ""
    for i in range(len(mystring)):
        if i % 2 ==0:
            result = result + mystring[i]
    return result

print(stringBits("HeLLo"))
print(stringBits("Hi"))
print(stringBits("Heeololeo"))


def ent_other(a, b):
    a = a.lower()
    b = b.lower()

    return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):]