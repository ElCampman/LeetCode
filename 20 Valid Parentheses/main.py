


record = []
case1 = "()"
case2 = "([)"
case3 = "(([{}{}])[][()()])"

def matchingchar(char):
    match char:
        case ')':
            return '('
        case ']':
            return '['
        case '}':
            return '{'

def isValid(str):
    for char in str:
        if char in ['(','[','{']:
            record.append(char)
        elif char in [')', ']', '}']:
            if matchingchar(char) == record[len(record) -1]:
                record.pop()
            elif matchingchar(char) != record[len(record) -1]:
                    return False
        else:
            return False
    if len(record) != 0:
        return False
    else:
        return True


print(isValid(case2))