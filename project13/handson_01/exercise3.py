def get_guess():
    return list(input("What is your guess? "))

def generate_guess():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]

x = get_guess()
print(x)