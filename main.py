# AS37

vowels = ["a", "e", "i", "o", "u"]

def code(string):
    for i in range(0, len(string)):
        if string[i] not in vowels:
            string[i] = string[i] + "o" + string[i]
    return string


string = list(input("Input message"))
print(string)
print("".join(code(string)))
