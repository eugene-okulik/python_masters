words = {"I": 3, "love": 5, "Python": 1, "!": 50}

for key, val in words.items():
    for _ in range(val):
        print(key, end="")
    print()
