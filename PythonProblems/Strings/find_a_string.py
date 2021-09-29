def count_substring(string, sub_string):
    count = 0
    for index in range(len(string) - len(sub_string) + 1):
        current_substring = string[index:len(sub_string) + index]
        if current_substring == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
