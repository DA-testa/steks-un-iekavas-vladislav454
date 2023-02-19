from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(char, i+1))
        elif char in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                return i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, char):
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"


def main():
    input_type = input()
    if input_type == "I":
        text = input()
    elif input_type == "F":
        file_path = input()
        with open(file_path) as f:
            text = f.read().strip()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
