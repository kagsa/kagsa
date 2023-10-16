class ParseError(Exception):
    pass

def __init__(value, parseMemory):
    if (value != 'input') and (parseMemory[5] != ''):
        print(parseMemory[5])
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nKeywords must be at the beginning of the line')

    if value == 'input':
        if '|DATA1|' in parseMemory[5]:
            parseMemory[5] = parseMemory[5].replace('|DATA1|', 'input(|DATA-P|)|DATA1|')
        else:
            if parseMemory[5] == '':
                parseMemory[5] += '|DATA|'
            if '|DATA|' in parseMemory[5]:
                parseMemory[5] = parseMemory[5].replace('|DATA|', 'input(|DATA-P|)|DATA|')
            else:
                raise ParseError(f'can\'t parse (<file>, line {parseMemory[4]})')

    if value == 'var':
        parseMemory[5] = '|DATA0| = |DATA1|'

    if value == 'string':
        parseMemory[5] = '|DATA0| = str(|DATA1|)'

    if value == 'int':
        parseMemory[5] = '|DATA0| = int(|DATA1|)'

    if value == 'float':
        parseMemory[5] = '|DATA0| = float(|DATA1|)'

    if value == 'dict':
        parseMemory[5] = '|DATA0| = json.loads(|DATA1|)'

    if value == 'list':
        parseMemory[5] = '|DATA0| = list(|DATA1|)'

    if value == 'try':
        parseMemory[5] = 'try :'

    if value == 'catch':
        parseMemory[5] = 'except Exception as ERROR :'

    if value == 'for':
        parseMemory[5] = 'for |DATA| :'

    if value == 'if':
        parseMemory[5] = 'if |DATA| :'

    if value == 'elseif':
        parseMemory[5] = 'elif |DATA| :'

    if value == 'while':
        parseMemory[5] = 'while |DATA| :'

    if value == 'func':
        parseMemory[5] = 'def |DATA_N| |DATA| :'

    if value == 'class':
        parseMemory[5] = 'class |DATA-P| :'

    if value == 'else':
        parseMemory[5] = 'else :'

    if value in ['break', 'continue']:
        parseMemory[5] = value

    if value == 'return':
        parseMemory[5] = 'return |DATA|'

    return parseMemory
