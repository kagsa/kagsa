class ParseError(Exception):pass

def __init__ (value,parseMemory):
    # errors
    if 'else :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {line})\nCan\'t add any arguments to try command')
    
    value=value.replace(' ','')
    newValues={
        '->':' in ',
        '<=':'<=',
        '>=':'>=',
        '==':'==',
        '<':'<',
        '>':'>',
        '!=':'!=',
        '||':' or ',
        '&&':' and ',
        'true':' True ',
        'false':' False '
    }
    value = newValues[value]

    # if |DATA-P| not set yet
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|',value)
    # if |DATA| in line
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')
    # if var name not set yet
    elif '|DATA0|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA0|',f'{value}|DATA0|')
    # if this is var & is named
    elif '|DATA1|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
    elif parseMemory[5]=='':
        parseMemory[5]+=f'{value}|DATA|'
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')
    
    return parseMemory