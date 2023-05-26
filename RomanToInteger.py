def get_int(s: str) -> int:
    match s:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000
        case _:
            return -1


def roman_to_int(s: str) -> int:
    index: int = 0
    s_length: int = len(s) - 1
    result: int = 0
    next_char: str = ""

    while index <= s_length:
        curr_char = s[index]

        if index < s_length:
            next_char = s[index + 1]
        else:
            next_char = curr_char

        if get_int(curr_char) < get_int(next_char):
            result += get_int(next_char) - get_int(curr_char)
            index += 1
        else:
            result += get_int(curr_char)

        index += 1

    return result
