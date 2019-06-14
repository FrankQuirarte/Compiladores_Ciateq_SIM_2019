import collections
import re
DebugMessage = False
Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])
# -------------------------------------------------------------------------------------------------

def tokenize(code):
    keywords = {
        'auto', 'break', 'case', 'char', 'const', 'continue',
        'default', 'do', 'double', 'else', 'enum', 'extern',
        'float', 'for', 'goto', 'if', 'int', 'long',
        'register', 'return', 'short', 'signed', 'sizeof', 'static',
        'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
        'volatile', 'while'
    }
    # ----------------------------------------------------------------------------
    token_specification = [
        ('Identifier',             r'[A-Za-z]+'),    # Identifiers (eg: main, total),
        ('Constants',              r'\d+(\.\d*)?'),  # Integer or float number (eg: 10, 20),
        ('End_instrution',         r';'),            # Statement terminator
        ('Newline',                r'\n'),           # Line endings
        ('Skip',                   r'[ \t]+'),       # Skip over spaces and tabs
        ('Special_symbols',        r'[!\"#&\'\(\)\\\\,\.\/:<>?\[\]\^_\{\|\}~]'),  # Special symbols(eg: (), {})
        ('Assign',                 r'={1}'),         # Assignment operator
        ('Arithmetic_operators',   r'[\+\-\*\/%]'),  # Arithmetic operators (eg: +,/,-,*,%)
        ('Unknown',                r'.'),            # Any other character (except newline character)
    ]

    # ----------------------------------------------------------------------------
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    # ----------------------------------------------------------------------------
    print("**********Running Frank´s C lexer**********************")
    if DebugMessage:
        print(tok_regex)

    line_num = 0  # check
    line_start = 0

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'Constants':
            value = float(value) if '.' in value else int(value)
        elif kind == 'Identifier':
            if value in keywords:
                kind = 'Keyword'
            else:
                kind = 'Identifier'
        elif kind == 'Newline':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'Skip':
            continue
        elif kind == 'Special_symbols':
            kind = 'Special_symbol'
        elif kind == 'Assign':
            kind = 'Assign_operator'
        elif kind == 'Arithmetic_operators':
            kind = 'Arithmetic_operator'
        elif kind == 'Unknown':
            kind = 'Unknown_symbol'
            #raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)
        if DebugMessage:
            print(tok_regex)


# ------------------------------------------------------------------------------------
# example from: https://fresh2refresh.com/c-programming/c-tokens-identifiers-keywords/
statements = '''
int main()
{
   int x, y, total;
   x = 10, y = 20;
   total = x + y;
   printf ("Total = %d \n", total);
}
'''

for token in tokenize(statements):
    print(token)