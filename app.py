def reversed(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0, word)
    return " ".join(result)

user_input = raw_input("Enter a sentence: ")
print reversed(user_input)