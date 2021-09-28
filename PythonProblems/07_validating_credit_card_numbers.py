import re


def starts_with_valid_number(credit_card_number):
    return int(credit_card_number[0]) in [4, 5, 6]


def valid_length(credit_card_number):
    if "-" in credit_card_number:
        credit_card_number = "".join(credit_card_number.split("-"))
    return True if len(credit_card_number) == 16 else False


def contains_only_digits(credit_card_number):
    if "-" in credit_card_number:
        credit_card_number = "".join(credit_card_number.split("-"))
    return all(x.isdigit() for x in credit_card_number)


def not_repeating_chars(credit_card_number):
    if "-" in credit_card_number:
        credit_card_number = "".join(credit_card_number.split("-"))
    for ch in range(len(credit_card_number) - 3):
        four = [credit_card_number[ch],
                credit_card_number[ch + 1],
                credit_card_number[ch + 2],
                credit_card_number[ch + 3]]
        if len(set(four)) == 1:
            return False
    return True


def consecutive_numbers(credit_card_number):
    return re.search(r"\b[0-9]{4}-{,1}[0-9]{4}-{,1}[0-9]{4}-{,1}[0-9]{4}", credit_card_number)


def is_card_valid(credit_card_number):
    return starts_with_valid_number(credit_card_number) and \
           valid_length(credit_card_number) and \
           contains_only_digits(credit_card_number) and \
           not_repeating_chars(credit_card_number) and \
           consecutive_numbers(credit_card_number)


n = int(input())
credit_cards = [input() for _ in range(n)]
card = credit_cards[2]

for card in credit_cards:
    if is_card_valid(card):
        print("Valid")
    else:
        print("Invalid")
