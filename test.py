import main

count = 0

RED = '\033[31m'
END = '\033[0m'

def test(target, expect):
    global count
    if target == expect:
        print(f'test{count} is OK')
    else: 
        print(f'test{count} is {RED}NG{END}')
        print(f'  Expected `{expect}`, but got `{target}`')

    count += 1

def test_print(target):
    print("===DEBUG===")
    print(target)
    print("===DEBUG===")

test(main.is_reserved_symbol('('), True)
test(main.is_reserved_symbol(')'), True)
test(main.is_reserved_symbol('+'), True)
test(main.is_reserved_symbol(' '), False)
test(main.is_reserved_symbol('a'), False)
test(main.is_reserved_symbol('()'), False)

test(main.is_space(' '), True)
test(main.is_space('a'), False)

# tokenize
test(main.tokenize('(a b c)'), ['(', 'a', 'b', 'c', ')'])
test(main.tokenize('(foo bar baz)'), ['(', 'foo', 'bar', 'baz', ')'])
test(main.tokenize('((foo bar baz))'), ['(', '(', 'foo', 'bar', 'baz', ')', ')'])
test(main.tokenize('((foo bar) baz)'), ['(', '(', 'foo', 'bar', ')', 'baz', ')'])

# parse
test(main.parse(['(', '+', 'foo', 'bar', ')']), ['+', 'foo', 'bar'])  # 12
test(main.parse(['(', '(', 'foo', 'bar', ')', 'baz', ')']), [['foo', 'bar'], 'baz']) # 13
test(main.parse(['(', '+', '(', '+', '1', '2', ')', '3', ')']), ['+', ['+', 1, 2], 3]) # 14

# eval
test(main.eval(['+', 1, 2]), 3)  # 15
test(main.eval(['+', ['+', 1, 2], 3]), 6)  # 16
test(main.eval(['+', ['-', 1, 2], 3]), 2)  # 17
test(main.eval(['*', ['-', 1, 2], 3]), -3)  # 18
test(main.eval(['/', ['+', 1, 2], 3]), 1)  # 19


