import regex as re  # pip install regex

with open("1/input.txt", newline="") as f:
    lines = f.readlines()

# Part 1

numbers = []
for line in lines:
    digits = re.findall(r"[0-9]", line)
    if digits:
        numbers.append(int(digits[0] + digits[-1]))
print(sum(numbers))


# Part 2

NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
digits_str = f"[0-9]|{'|'.join(NUMBER_MAP.keys())}"


def convert_to_digit(x):
    try:
        return str(NUMBER_MAP[x])
    except KeyError:
        return x


numbers = []
for line in lines:
    digits = re.findall(digits_str, line, overlapped=True)
    print(digits)
    if digits:
        first = convert_to_digit(digits[0])
        last = convert_to_digit(digits[-1])
        numbers.append(int(first + last))
print(sum(numbers))
