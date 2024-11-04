def get_guess():
    return list(input("What is your guess? "))

def generate_code():
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


print("Welcome Code Broker")
secret_code = generate_clues()
clue_report =[]
while clue_report != "Code Cracked":
    guess = get_guess()