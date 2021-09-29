import re


def has_two_letters(word):
    return re.search(r"[A-Z].*[A-Z]", word)


def has_three_numbers(word):
    return re.search(r"[0-9].*[0-9].*[0-9]", word)


n = int(input())
for _ in range(n):
    uid = input()
    if has_two_letters(uid) and \
            has_three_numbers(uid) and \
            uid.isalnum() and \
            len(set(uid)) == len(uid) and \
            len(uid) == 10:
        print("Valid")
    else:
        print("Invalid")
