def __init__ (value,parseMemory):
    value=value.replace(' ','')
    if 'else :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to try command')
    
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|','')
    elif ('|DATA1|' in parseMemory[5]) and (parseMemory[6] == False):
            raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nVariable opened without assign')
    elif '|DATA1|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')
    elif parseMemory[5]=='':
        parseMemory[5]+=f'{value}|DATA|'
    else:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nUnknown place of math symbol')
    
    return parseMemory