word = input("type a word")
is_palind = True
for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palind = False
        break


if is_palind:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
