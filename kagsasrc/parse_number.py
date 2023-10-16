class ParseError(Exception):
    pass

def __init__(value, parseMemory):
    if parseMemory[7] == 'else':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to else command')

    if parseMemory[7] == 'catch':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to catch command')

    if parseMemory[7] == 'try':
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to try command')

    if value.replace('0', '') != '':
        while True:
            if value.startswith('0'):
                value = value[1:]
            else:
                break

        if value == '':
            raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nNumber can\'t be zero')

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
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown place for number')

    return parseMemory
