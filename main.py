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


# Reference: https://samurait.hatenablog.com/entry/lisp_interpreter_implementation_in_python
def parse(tokens):
    if len(tokens) == 0:
        raise SyntaxError("Unexpected EOF while reading")
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError("Unexpected")
    else:
        return atom(token)

def atom(token):
    try: return int(token)
    except ValueError:
        try:
            return float(token)
        except:
            return Symbol(token)


Symbol = str
Number = (int, float)

#def parse(tokens):
#    # Check parenthesis '()' number
#    if tokens.count('(') != tokens.count(')'):
#        #print("ERROR: No match () number", end=' ')
#        return []
#
#    ast = []
#    i = 0
#    max = len(tokens)
#    while i < max:
#        if tokens[i] == '(':
#            ast_tmp, count = parse(tokens[i+1:])
#            ast.append(ast_tmp)
#            i += count + 1
#            continue
#
#        if tokens[i] == ')':
#            i += 1
#            break
#
#        ast.append(tokens[i])
#        i += 1
#
#    return ast, i


# TODO: implement
def eval(ast):
    stack = []

    if len(ast) == 0:
        print("ERROR: Somewhre in parse process.")

    for expr in ast:
        stack.append(expr)

    operator = stack.pop(0)
    lhs = stack.pop(0)
    rhs = stack.pop(0)

    # Recursive evaluate
    if type(lhs) == list:
        lhs = eval(lhs)

    if type(rhs) == list:
        rhs = eval(rhs)

    if operator == '+':
        return lhs + rhs
    elif operator == '-':
        return lhs - rhs
    elif operator == '*':
        return lhs * rhs
    elif operator == '/':
        return lhs / rhs

    return result



if __name__ == '__main__':
    while True:
        input_str = input("(lisp)> ")
        tokens = tokenize(input_str)
        ast = parse(tokens)
        ans = eval(ast)
        print(f'ans => {ans}')
