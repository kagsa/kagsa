from .parse_endl import parse_endl as parse_endl

def parse_cparen(value, parseMemory):
    parseMemory[5] = parseMemory[5].replace('|DATA-P|', '')

    if value == '{':
        parseMemory[1] = True
    else:
        parseMemory[1] = False
        if parseMemory[0] == 0:
            raise SyntaxError('invalid syntax (<file>, line ' + str(parseMemory[4]) + ')\nunknown place for }')
        parseMemory[0] -= 1
    
    parseMemory = parse_endl('\n', parseMemory, addline=False)
    return parseMemory
