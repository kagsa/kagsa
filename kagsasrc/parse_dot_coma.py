class ParseError (Exception):pass

def __init__ (value,parseMemory):
    # catch error
    if 'else :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]:
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to try command')
    
    # if |DATA-P| is empty : close it
    if '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|','')
    # if |DATA| found
    if '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')
    #
    elif ('|DATA1|' in parseMemory[5]) and (parseMemory[6] == False):
        parseMemory[5]=parseMemory[5].replace('|DATA0|',f'{value}|DATA0|')
    # var items bar is opened
    elif ('|DATA1|' in parseMemory[5]):
        parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')
    
    return parseMemory