def is_leap(year_to_check):
    if year_to_check % 4 == 0:
        if year_to_check % 100 == 0:
            if year_to_check % 400 == 0:
                return True
            return False
        return True
    return False


year = int(input())
print(is_leap(year))
