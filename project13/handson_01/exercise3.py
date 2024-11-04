def get_guess():
    return list(input("What is your guess? "))

def generate_guess():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]

def generate_clues(code, user_guess):
    if user_guess == code:
        return "Code Cracked!"
    
    clues = []
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

x = get_guess()
print(x)