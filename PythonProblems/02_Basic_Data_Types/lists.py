def main(lines):
    result = []
    for _ in range(lines):
        line_args = input().split()
        command = line_args[0]

        if command == "insert":
            idx = int(line_args[1])
            el = int(line_args[2])
            result.insert(idx, el)
        elif command == "print":
            print(result)
        elif command == "remove":
            el = int(line_args[1])
            result.remove(el)
        elif command == "append":
            el = int(line_args[1])
            result.append(el)
        elif command == "sort":
            result.sort()
        elif command == "pop":
            result.pop()
        elif command == "reverse":
            result = result[::-1]


if __name__ == '__main__':
    n = int(input())
    main(n)
