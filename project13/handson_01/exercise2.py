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

    # return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]

print(ent_other("Hiabc", "abc"))
print(ent_other("Abc", "HiaBc"))
print(ent_other("abc", "abXabc"))

def doubleChar(mystring):
    result = ""
    for char in mystring:
        result += char * 2
    return result

print(doubleChar("The"))

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
    

def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))