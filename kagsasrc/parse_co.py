class ParseError(Exception):
    pass

def parse_co(value, parseMemory):
    # Check for errors
    if parseMemory[7] == 'else':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to else command')
    if parseMemory[7] == 'catch':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to catch command')
    if parseMemory[7] == 'try':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to try command')
    
    # Remove spaces
    value = value.replace(' ', '')

    newValues = {
        '->': ' in ',
        '<=': '<=',
        '>=': '>=',
        '==': '==',
        '<': '<',
        '>': '>',
        '!=': '!=',
        '||': ' or ',
        '&&': ' and ',
        'true': ' True ',
        'false': ' False '
    }

    # Replace values with their Python equivalents
    value = newValues[value]

    # Handle different cases for parsing
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA-P|', value)
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA|', f'{value}|DATA|')
    elif '|DATA0|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA0|', f'{value}|DATA0|')
    elif '|DATA1|' in parseMemory[5]:
        parseMemory[5] = parseMemory[5].replace('|DATA1|', f'{value}|DATA1|')
    elif parseMemory[5] == '':
        parseMemory[5] += f'{value}|DATA|'
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')

    return parseMemory
