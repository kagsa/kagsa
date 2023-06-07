
def __init__ (value, parseMemory):

    if (parseMemory[7] == 'else'):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to else command')
    if (parseMemory[7] == 'catch'):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to catch command')
    if (parseMemory[7] == 'try'):
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\ncan\'t add any arguments to try command')
    
    if '|DATA_N|' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nComplete function sentence')
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|','')
    if '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')
    elif '|DATA0|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA0|',f'{value}|DATA0|')
    elif '|DATA1|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
    else:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown place of paren')
    
    return parseMemory