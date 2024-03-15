
def is_reserved_symbol(char):
    if char == '(' or ')' or '+' or '-':
        return True

    return False

def lexer(input_str):
    ret_list = []
    tmp_str = ""
    for c in input_str:
        if isspace(c):
            continue
        else:
            tmp_str += c # variable name
            continue

        ret_list.append(c)
        tmp_str = "" # Reset

    return ret_list


while True:
    input_str = input("(lisp)> ")
    ans = lexer(input_str)
    print(ans)
