str = input("enter a stirng in lowercase.:")
for vowel in "aeo":
    if vowel in str:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
