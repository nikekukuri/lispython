import copy

def is_reserved_symbol(char):
    if char == '(':
        return True
    elif char == ')':
        return True
    elif char == '+':
        return True
    elif char == '-':
        return True

    return False


def is_space(char):
    if char == ' ':
        return True

    return False


def tokenize(input_str):
    tokens = input_str.split(' ')

    ## Split '(foo' -> '(', 'foo'
    for i, token in enumerate(tokens):
        if token.startswith('('):
            tokens[i] = '('
            tokens.insert(i+1, token[1:])

    tokens_tmp = copy.deepcopy(tokens)
    offset = 0
    for i, token in enumerate(tokens_tmp):
    ## Split 'foo)' -> 'foo', ')'
        if token.endswith(')'):
            cnt = token.count(')')
            tokens[i+offset] = token[:-cnt]
            for c in range(cnt):
                tokens.insert(i+offset+c+1, ')')
            offset += cnt
    
    return tokens


def parse(tokens, ast):
    # check parenthesis '()' number
    if tokens.count('(') != tokens.count(')'):
        #print("ERROR: No match () number", end=' ')
        return []

    ast_tmp = []
    for i, token in enumerate(tokens):
        if token == '(':
            parse(tokens[i+1:], ast)
            continue

        if token == ')':
            break

        ast_tmp.append(token)

    ast.append(ast_tmp)
    return ast


# TODO: implement
def eval(ast):
    if len(ast) == 0:
        print("ERROR: anywhre parse process.")

    return ast

if __name__ == '__main__':
    while True:
        input_str = input("(lisp)> ")
        tokens = tokenize(input_str)
        ast = []
        ast = parse(tokens, ast)
        ans = eval(ast)
        print(ans)
